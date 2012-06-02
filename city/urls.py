from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import index, view, create, save, CreateCityWizard
from forms import CityForm, ThemeThreatForm, LocationForm, FaceForm
import os.path

WEB_ROOT = os.path.join( os.path.dirname( __file__), '/web')
APP_ROOT = os.path.join( os.path.dirname( __file__), '/web/city')

urlpatterns = patterns('city.views',
	url(r'^$', index),
	url(r'^(?P<city_id>\d+)/$', view),
	url(r'^create/$', CreateCityWizard.as_view([CityForm, ThemeThreatForm, ThemeThreatForm, ThemeThreatForm, LocationForm, FaceForm])), 
	url(r'^save/$', save), 
)
