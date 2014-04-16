from django.conf.urls.defaults import patterns, include, url

from main_site import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'uptime/$', views.uptime, name='uptime'),
    url(r'work/$', views.work, name='work'),
    url(r'links/$', views.links, name='links'),
    url(r'^threaded/$', views.threaded, name='threaded'),
    url(r'^new-year/$', views.new_year, name='new_year'),
)
