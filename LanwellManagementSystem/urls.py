from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from LDMSystemMain.views import PersonsListView,PersonDetailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'LDMSystemMain.views.index', name='index'),
    #url(r'^persons/$', PersonsList.as_view()),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<slug>[-_\w]+)/$', PersonDetailView.as_view(), name='person-detail'),

    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #TODO: Development
