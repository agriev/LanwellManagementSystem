from django.db import models
from django.forms import ModelForm

# Create your models here.
# class Superparent(models.Model):  # Holds AutoId
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


#DONE: Person Assignment Remove
#DONE: TASK Add
#DONE: Task Remove
#TODO: Person Assigment make to existing task
class Person(Item, Executive):
    first_name = models.CharField(verbose_name="Имя", max_length=30)
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    experience = models.IntegerField(default=0, verbose_name="Опыт")
    rating = models.IntegerField(verbose_name="Рейтинг", default=0)
    description = models.TextField(default="", verbose_name="Описание")
    phone = models.CharField(verbose_name="Телефон", default="", max_length=20)
    email = models.EmailField(verbose_name="e-mail", default="", max_length=30)
    skills = models.ManyToManyField("LDMSystemMain.Skill", verbose_name="Навык", blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " id: " + str(self.executive_id)


class Skill(Item):
    name = models.CharField(verbose_name="Название", max_length=30)
    description = models.CharField(verbose_name="Описание", max_length=30)

    def __str__(self):
        return self.name


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





#DONE: Task List
#DONE: Task Edit
#TODO: Existing Task Assign
class Task(Item):
    NEW = "NEW"
    TASK_STATUS_CHOICES = (
        ("NEW", "NEW"),
        ("ASSIGNED", "ASSIGNED"),
        ("IN_PROGRESS", "IN PROGRESS"),
        ("COMPLETED", "COMPLETED"),
        ("CANCELED", "CANCELED"),
    )
    # PAYMENT_OPTIONS = ( #TODO: Разные варианты оплаты
    # ("ONCOMPLETE", "ON COMPLETION"),
    #     ("PARTIAL", "BY PARTS"),
    #     ("REGULAR", "REGULAR PAYMENTS"),
    # )
    name = models.CharField(max_length=30)
    datestart = models.DateTimeField(verbose_name="Дата начала", auto_now=True, null=True)
    datefinish = models.DateTimeField(verbose_name="Дата завершения", auto_now=True, null=True)
    duration = models.IntegerField()
    person = models.ManyToManyField(Executive, through='Assigment')
    parent = models.ForeignKey("self", verbose_name="Родительская задача", null=True)  # TODO: Construct
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default=NEW)
    is_project = models.BooleanField(default=False, verbose_name="Является проектом")

    def __str__(self):
        return self.name + " "  # + self.person.executive_id

    def isProject(self):
        return False


class Project(Task):  # TODO: Base fixture
    #name = models.CharField(max_length=30)
    def isProject(self):
        return True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_project = True

    def __str__(self):
        return self.name


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'duration', 'status']


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


