from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import *
from forms import CityForm, ThemeThreatForm, LocationFormSet, FaceFormSet
import os.path

WEB_ROOT = os.path.join( os.path.dirname( __file__), '/web')
APP_ROOT = os.path.join( os.path.dirname( __file__), '/web/city')

urlpatterns = patterns('city.views',
	url(r'^$', index),
	url(r'^(?P<city_id>\d+)/$', view),
	url(r'^(?P<city_id>\d+)/themesorthreats/add$', theme_or_threat),
	url(r'^(?P<city_id>\d+)/themesorthreats/edit/(?P<theme_threat_id>\d+)$', theme_or_threat),
	url(r'^(?P<city_id>\d+)/locations/add$', location_form),
	url(r'^(?P<city_id>\d+)/locations/edit/(?P<location_id>\d+)$', location_form),
	url(r'^(?P<city_id>\d+)/faces/add$', face_form),
	url(r'^(?P<city_id>\d+)/faces/edit/(?P<face_id>\d+)$', face_form),
#	url(r'^create/$', CreateCityWizard.as_view([CityForm, ThemeThreatForm, ThemeThreatForm, ThemeThreatForm, LocationFormSet, FaceFormSet])), 
	url(r'^create$', city_form),
)
