from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('main_site.urls'), name="main_site"),
    url(r'^hiking[/]?$', include('hiking.urls', namespace="hiking"), ),

    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': "%s/main_site/fonts" % settings.STATIC_ROOT,
    }),
    url(r'^admin/', include(admin.site.urls)),
)
