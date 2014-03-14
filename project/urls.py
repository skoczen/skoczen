from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('main_site.urls', namespace="main_site"), ),
    url(r'^manual/', include('manual.urls', namespace="manual"), ),
    url(r'^hiking/', include('hiking.urls', namespace="hiking"), ),
    url(r'^resume/', include('resume.urls', namespace="resume"), ),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': "%s/main_site/fonts" % settings.STATIC_ROOT,
    }),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
