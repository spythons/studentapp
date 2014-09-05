from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home', 'studentapp.views.home', name='home'),
    url(r'^displaystudent','studentapp.views.displaystudent', name='displaystudent'),
    url(r'^updatestudent','studentapp.views.updatestudent',name='updatestudent'),

    url(r'^admin/', include(admin.site.urls)),
    
)
