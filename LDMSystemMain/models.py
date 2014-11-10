from django.db import models
from django.forms import ModelForm

# Create your models here.
#class Superparent(models.Model):  # Holds AutoId
#    pass


class Item(models.Model):  # Всё у чего есть камменты
    item_id = models.AutoField(primary_key=True)
    pass


class Executive(models.Model):  # Всё что может являться исполнителем - основной ID для исполнителей
    executive_id = models.AutoField(primary_key=True)

    def __str__(self):
        print(type(self))
        if Person.objects.filter(executive_id=self.executive_id):
            return str(Person.objects.get(executive_id=self.executive_id))
        else:
            return " %d" % self.executive_id

#TODO: Person Assignment
# TODO: TASK Add
#DONE: Task Remove
class Person(Item, Executive):
    first_name = models.CharField(verbose_name="Имя", max_length=30)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    experience = models.IntegerField(default=0, verbose_name="Опыт")
    description = models.TextField(default="", verbose_name="Описание")
    phone = models.CharField(verbose_name="Телефон", default="", max_length=20)
    email = models.CharField(verbose_name="e-mail", default="", max_length=30)
    def __str__(self):
        return self.first_name + " " + self.last_name + " id: " + str(self.executive_id)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


#TODO: Company List
#TODO: Company Edit
class Company(Item, Executive):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

#TODO: Task List
#TODO: Task Edit
#TODO: Task Assign
class Task(Item):
    name = models.CharField(max_length=30)
    duration = models.IntegerField()
    person = models.ManyToManyField(Executive, through='Assigment')

    def __str__(self):
        return self.name + " "  # + self.person.executive_id


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'duration']

class Assigment(models.Model):
    person = models.ForeignKey(Executive)
    task = models.ForeignKey(Task)
    date_assigned = models.DateTimeField(auto_now=True)

#TODO: Comment person
#TODO: Comment task
#TODO: Comment company
class Comment(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    parent_item = models.ForeignKey(Item)


