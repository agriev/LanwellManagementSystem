from django.contrib import admin

from LDMSystemMain.models import Person, Task, Assigment, Comment, Company, Project, Skill



# Register your models here.
admin.site.register(Skill)
admin.site.register(Person)
admin.site.register(Task)
admin.site.register(Assigment)
admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(Project)
