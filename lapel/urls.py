from django.conf.urls import patterns, include, url
from django.contrib import admin
import application.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'application.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'application.views.index', name='index'),
    url(r'^send/$', 'application.views.send', name='send'),
)
