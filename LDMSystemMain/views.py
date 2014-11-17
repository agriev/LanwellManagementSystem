from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView

from LDMSystemMain.models import Person, Task, Company, PersonForm, TaskForm, Assigment, Skill








# Create your views here.
def index(request):
    persons = Person.objects.first()
    count_persons = Person.objects.count()
    count_tasks = Task.objects.count()
    # task = Task(name="sdfsdf", duration=50)
    #task.save()
    #assign1= Assigment(person=persons,task=task)
    #assign1.save()
    #task.person.add(Person.objects.all())
    #output = ',  '.join([p.first_name + ' ' + p.last_name for p in persons])
    return render_to_response('index.html', {"persons": count_persons, "tasks": count_tasks})
    # return HttpResponse(output)


class PersonsListView(ListView):
    # model = Person
    queryset = Person.objects.order_by('-rating')
    context_object_name = 'persons_list'


def personDetails(request, in_executive_id, error_form=""):
    if request.method == "GET":
        if in_executive_id == "0":  # ########## TODO: Избавиться от чёртового говонокода, иначе пиздец. Ну как так можно создавать сущности??? Когда ID=0 - новый инстанс создаём
            current = Person()
            isNew = True
            #current.save()
            form = PersonForm(instance=current)
            if error_form:
                form = error_form
            tasks = []
            task_form = TaskForm()
            return render(request, 'person_details.html',
                      {'current': current,
                       'string_cur': current.__str__(),
                       'form': form,  # Форма редактирования персоны
                       'tasks': tasks,  # Persons tasks
                       'task_form': task_form,
                       'is_new': isNew})  # New Task
        else:
            isNew = False
            current = get_object_or_404(Person, executive_id=in_executive_id)
            form = PersonForm(instance=current)
            if error_form:
                form = error_form
            # if Person.objects.filter(executive_id=executive_id):
            # current = Person.objects.filter(executive_id=executive_id)
            # else:
            # current = 0
            tasks = current.task_set
            task_form = TaskForm()
            return render(request, 'person_details.html',
                          {'current': current,
                           'string_cur': current.__str__(),
                           'form': form,  # Форма редактирования персоны
                           'tasks': tasks,  # Persons tasks
                           'task_form': task_form,
                           'is_new': isNew})  # New Task
    elif request.method == "POST":
        current = get_object_or_404(Person, executive_id=in_executive_id)
        form = PersonForm(request.POST, instance=current)
        if form.is_valid():
            person = form.save()
            request.method = "GET"
            return personDetails(request, in_executive_id=in_executive_id)
            # render(request, 'person_details.html', {'form': form})
        else:
            request.method = "GET"
            return personDetails(request, in_executive_id=in_executive_id, error_form=form)

            #return render(request, 'person_details.html', {'form': form})


def personAdd(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return HttpResponseRedirect("/person/%d/" % person.executive_id)
        else:
            request.method = "GET"

            return personDetails(request, in_executive_id="0", error_form=form)


class PersonDetailView(DetailView):  #DEPRECATED:
    model = Person

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['task_list'] = Task.objects.filter(person=self.object)
        return context


class CompanyListView(ListView):
    model = Company
    context_object_name = 'company_list'


class TasksListView(ListView):
    model = Task
    context_object_name = 'tasks_list'


def taskDetails(request, in_item_id, errorForm=""):  # TODO: Refactor if in_item_id=0 then - NewTask
    if request.method == "GET":
        if in_item_id == "0":
            current = Task()
            current.item_id = "0"
            if errorForm:
                form = errorForm
            else:
                form = TaskForm()
            return render(request, 'task_details.html',
                          {'current': current, 'form': form})
        else:
            current = get_object_or_404(Task, item_id=in_item_id)
            form = TaskForm(instance=current)
            # if Person.objects.filter(executive_id=executive_id):
            # current = Person.objects.filter(executive_id=executive_id)
            # else:
            # current = 0
            return render(request, 'task_details.html',
                          {'current': current, 'string_cur': current.__str__(), 'form': form})
    elif request.method == "POST":
        if in_item_id == "0":
            return taskAdd(request)
        else:
            current = get_object_or_404(Task, item_id=in_item_id)
            form = TaskForm(request.POST, instance=current)
            if form.is_valid():
                current = form.save()
                return render(request, 'task_details.html', {'current': current, 'form': form})
            else:
                current = Task()
                current.item_id = in_item_id
                request.method = "GET"
                return render(request, 'task_details.html', {'current': current, 'form': form})


def taskAdd(request,
            in_executive_id=""):  # Фактически добавляет задачу на исполнителя, логика просто добавления задачи - излишня
    if request.method == "POST":
        form = TaskForm(request.POST)  # , instance=current)
        if form.is_valid():
            task = form.save()
            if in_executive_id:
                person = get_object_or_404(Person, executive_id=in_executive_id)  # TODO: Not only Person is executive
                assigment = Assigment(person=person, task=task)
                assigment.save()
                return HttpResponseRedirect('/person/' + in_executive_id + '/')
            else:
                request.method = "GET"
                return taskDetails(request, in_item_id=task.item_id)
        else:
            if in_executive_id:
                return personDetails(request, in_executive_id=in_executive_id)
            else:
                request.method = "GET"
                return taskDetails(request, in_item_id="0", errorForm=form)


def assigmentEdit(request, in_item_id, command):
    if request.method == "POST":
        if command == "delete":
            task_id = in_item_id
            executive_id = request.POST["executive_id"]
            Assigment.objects.filter(person_id=executive_id, task_id=task_id).delete()
            # print ("Deleted")
            return HttpResponse("200 OK")


def bySkillPersonView(request):  # #TODO: Переверстать вьюху
    skills = Skill.objects.all()
    output = {}
    for skill in skills:
        output[skill] = skill.person_set.all()
    return render_to_response("by_skill_person.html", {"skills": skills, "persons": output})


class CommentListView(ListView):
    model = Company
    context_object_name = 'comment_list'

