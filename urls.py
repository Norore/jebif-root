
from django.conf.urls import patterns, include
#from django.conf.urls.defaults import *
# django.conf.urls.defaults removed from django 1.4
from django.contrib import admin
from django.views.generic import RedirectView
from jebif import settings

admin.autodiscover()

urlpatterns = patterns('',
    # add 'django.contrib.admindocs' to INSTALLED_APPS 
    # to enable admin documentation
    # (r'^admin/doc/',    include('django.contrib.admindocs.urls')),
    (r'^cv/',			include('cv.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^accounts/', include('django.contrib.auth.urls')),
    (r'^election/', include('election.urls')),
    (r'^membership/', include('membership.urls')),
    (r'^$', RedirectView.as_view(url='http://jebif.fr')),
)
