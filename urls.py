
#from django.conf.urls import *
from django.conf.urls.defaults import *
# django.conf.urls.defaults removed from django 1.4
from django.contrib import admin
from django.contrib.auth import urls
from django.views.generic import RedirectView
from django.views.static import serve

from jebif import settings

admin.autodiscover()

urlpatterns = [
    # add 'django.contrib.admindocs' to INSTALLED_APPS 
    # to enable admin documentation
    # (r'^admin/doc/',    include('django.contrib.admindocs.urls')),

    (r'^admin/',        include(admin.site.urls)),
    (r'^admin_media/(?P<path>.*)$', serve, {'document_root': settings.ADMIN_MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

	(r'^accounts/',		include(urls)),
    #	(r'^cv/',			include('cv.urls')),
	(r'^election/', 	include('election.urls')),
	(r'^membership/', 	include('membership.urls')),

	(r'^$', RedirectView.as_view(url='http://jebif.fr'))
]

