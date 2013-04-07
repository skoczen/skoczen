from django.conf.urls.defaults import patterns, include, url

from manual import views

import dselector
parser = dselector.Parser()
url = parser.url

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^daily$', views.daily, name='daily'),
    url(r'^daily_form/{day_pk:digits}/', views.daily_form, name='daily_form'),
    url(r'^monthly$', views.monthly, name='monthly'),
    url(r'^update_bumpers/{bumper_pk:digits}/', views.update_bumpers, name='update_bumpers'),
    url(r'^get_sleep_hrs/{bumper_pk:digits}/', views.get_sleep_hrs, name='get_sleep_hrs'),


    url(r'^emotions', views.emotions, name='emotions'),
    url(r'^emotion/{emotion_slug:slug}/', views.emotion, name='emotion'),
    url(r'^values', views.values, name='values'),
    url(r'^value/{value_slug:slug}/', views.value, name='value'),

    url(r'^eighty', views.eighty, name='eighty'),
    
    url(r'^singly_callback', views.singly_callback, name='singly_callback'),
    url(r'^fitbit_callback', views.fitbit_callback, name='fitbit_callback'),
    

)
