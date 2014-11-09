from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView

from LDMSystemMain.models import Person, Task, Company, PersonForm, TaskForm, Assigment






# Create your views here.
def index(request):
    persons = Person.objects.first()
    # task = Task(name="sdfsdf", duration=50)
    #task.save()
    #assign1= Assigment(person=persons,task=task)
    #assign1.save()
    #task.person.add(Person.objects.all())
    #output = ',  '.join([p.first_name + ' ' + p.last_name for p in persons])
    return render_to_response('index.html', persons)
    # return HttpResponse(output)


class PersonsListView(ListView):
    model = Person
    context_object_name = 'persons_list'


def personDetails(request, in_executive_id):
    if request.method == "GET":
        current = get_object_or_404(Person, executive_id=in_executive_id)
        form = PersonForm(instance=current)
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
                       'task_form': task_form})  # New Task
    elif request.method == "POST":

        current = get_object_or_404(Person, executive_id=in_executive_id)
        form = PersonForm(request.POST, instance=current)
        form.save()
        return render(request, 'person_details.html', {'form': form})


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


def taskDetails(request, in_item_id):
    if request.method == "GET":
        current = get_object_or_404(Task, item_id=in_item_id)
        form = TaskForm(instance=current)
        # if Person.objects.filter(executive_id=executive_id):
        # current = Person.objects.filter(executive_id=executive_id)
        # else:
        # current = 0
        return render(request, 'task_details.html',
                      {'current': current, 'string_cur': current.__str__(), 'form': form})
    elif request.method == "POST":

        current = get_object_or_404(Task, item_id=in_item_id)
        form = TaskForm(request.POST, instance=current)
        form.save()
        return render(request, 'task_details.html', {'form': form})


def assigmentEdit(request, in_item_id, command):
    if request.method == "POST":
        if command == "delete":
            task_id = in_item_id
            executive_id = request.POST["executive_id"]
            Assigment.objects.filter(person_id=executive_id, task_id=task_id).delete()
            # print ("Deleted")
            return HttpResponse("200 OK")

class CommentListView(ListView):
    model = Company
    context_object_name = 'comment_list'

