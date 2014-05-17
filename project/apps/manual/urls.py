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
    url(r'^one-thing', views.todays_one_thing, name='todays_one_thing'),
    url(r'^weights', views.last_10_weights, name='last_10_weights'),
    url(r'^red-flags/drinking', views.red_flag_drinking, name='red_flag_drinking'),

    url(r'^correlations', views.correlations, name='correlations'),
    url(r'^correlations-for/{item:slug}/', views.correlations_for, name='correlations_for'),
    url(r'^dump', views.data_dump, name='data_dump'),

)
