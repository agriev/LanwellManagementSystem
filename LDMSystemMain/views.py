from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from LDMSystemMain.models import Person,Task,Assigment,Company,Comment
from django.views.generic import ListView,DetailView


# Create your views here.
def index(request):
    persons = Person.objects.all()

    output = ',  '.join([p.first_name + ' ' + p.last_name for p in persons])
    return render_to_response('index.html', persons)
    #return HttpResponse(output)

class PersonsListView(ListView):
    model = Person
    context_object_name = 'persons_list'

class PersonDetailView(DetailView):
    model = Person
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PersonDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['task_list'] = Task.objects.filter(person=self.object)
        return context



class CompanyListView(ListView):
    model = Company
    context_object_name = 'company_list'

class TaskListView(ListView):
    model = Task
    context_object_name = 'task_list'

class CommentListView(ListView):
    model = Company
    context_object_name = 'comment_list'

