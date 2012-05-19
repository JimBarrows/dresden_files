from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import index 
import os.path

WEB_ROOT = os.path.join( os.path.dirname( __file__), '/web')
APP_ROOT = os.path.join( os.path.dirname( __file__), '/web/city/create')

urlpatterns = patterns('city_creation.views',
	url(r'^$', index),
)
