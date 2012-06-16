from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^core/', include( 'core.urls')),
	url(r'^city/', include( 'city.urls')),
	url(r'^character/', include( 'character.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$',index),
)
