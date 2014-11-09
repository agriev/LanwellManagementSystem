from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from LDMSystemMain.views import PersonsListView, TasksListView


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'LDMSystemMain.views.index', name='index'),
    url(r'^persons/$', PersonsListView.as_view()),
    url(r'^tasks/$', TasksListView.as_view()),
    # url(r'^blog/', include('blog.urls')),
    url(r'^person/(?P<in_executive_id>\d+)/$', 'LDMSystemMain.views.personDetails', name='person-detail'),
    url(r'^task/(?P<in_item_id>\d+)/$', 'LDMSystemMain.views.taskDetails', name='task-detail'),
    url(r'^assigmentedit/(?P<in_item_id>\d+)/(?P<command>\w+)/$', 'LDMSystemMain.views.assigmentEdit',
        name='assigment-edit'),

    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #TODO: Development

