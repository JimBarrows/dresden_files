from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import *
from forms import *
import os.path

WEB_ROOT = os.path.join( os.path.dirname( __file__), '/web')
APP_ROOT = os.path.join( os.path.dirname( __file__), '/web/character')

urlpatterns = patterns('character.views',
	url(r'^$', index),
	url(r'^(?P<character_id>\d+)$', view),
	url(r'^create$', character_form),
	url(r'^edit$', character_form),
	url(r'^minor_milestone/(?P<character_id>\d+)$', minor_milestone),
	url(r'^significant_milestone/(?P<character_id>\d+)$', significant_milestone),
	url(r'^major_milestone/(?P<character_id>\d+)$', major_milestone),
)
