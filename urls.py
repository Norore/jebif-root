
from django.conf.urls import patterns, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth.views import password_reset

admin.autodiscover()

urlpatterns = patterns('',
    # add 'django.contrib.admindocs' to INSTALLED_APPS 
    # to enable admin documentation
    # (r'^admin/doc/',    include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'settings.ADMIN_MEDIA_ROOT'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'settings.MEDIA_ROOT'}),
    (r'^accounts/', include('django.contrib.auth.urls')),
    (r'^election/', include('election.urls')),
    (r'^membership/', include('membership.urls')),
    (r'^cv/', include('cv.urls')),
    (r'^$', RedirectView.as_view(url='https://jebif.fr')),
)
