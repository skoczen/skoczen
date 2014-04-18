from django.conf.urls.defaults import patterns, include, url

from main_site import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'uptime/$', views.uptime, name='uptime'),
    url(r'professional/$', views.work, name='work'),
    url(r'art-and-social/$', views.links, name='links'),
    url(r'^threaded/$', views.threaded, name='threaded'),
    url(r'^new-year/$', views.new_year, name='new_year'),
)
