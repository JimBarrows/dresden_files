from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import index, view
import os.path

WEB_ROOT = os.path.join( os.path.dirname( __file__), '/web')
APP_ROOT = os.path.join( os.path.dirname( __file__), '/web/city')

urlpatterns = patterns('city.views',
	url(r'^$', index),
	url(r'^(?P<city_id>\d+)/$', view),
)
