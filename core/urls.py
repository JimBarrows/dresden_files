from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from views import *
from forms import *
from models import *


urlpatterns = patterns('core.views',
	url(r'^templates$', ListView.as_view(model=Template, queryset=Template.objects.all().order_by('name'))),
	url(r'^templates/add$', CreateView.as_view(model=Template, success_url='/core/templates')),
	)
