from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import index, view, CreateCityWizard, faces, theme_or_threat
from forms import CityForm, ThemeThreatForm, LocationFormSet, FaceFormSet
import os.path

WEB_ROOT = os.path.join( os.path.dirname( __file__), '/web')
APP_ROOT = os.path.join( os.path.dirname( __file__), '/web/city')

urlpatterns = patterns('city.views',
	url(r'^$', index),
	url(r'^(?P<city_id>\d+)/$', view),
	url(r'^(?P<city_id>\d+)/themesorthreats/add$', theme_or_threat),
	url(r'^(?P<city_id>\d+)/themesorthreats/edit/(?P<theme_threat_id>\d+)$', theme_or_threat),
	url(r'^(?P<city_id>\d+)/faces$', faces),
	url(r'^create/$', CreateCityWizard.as_view([CityForm, ThemeThreatForm, ThemeThreatForm, ThemeThreatForm, LocationFormSet, FaceFormSet])), 
)
