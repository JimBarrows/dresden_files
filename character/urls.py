from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import *
from forms import *
import os.path

WEB_ROOT = os.path.join( os.path.dirname( __file__), '/web')
APP_ROOT = os.path.join( os.path.dirname( __file__), '/web/character')

urlpatterns = patterns('character.views',
	url(r'^$', CharacterListView.as_view()),
	url(r'^create$', ChooseATemplateFormView.as_view()),
	url(r'^create/choose_a_template$', ChooseATemplateFormView.as_view()),
	url(r'^create/choose_power_level/(?P<pk>\d+)$', ChooseAPowerLevelFormView.as_view()),
	url(r'^create/high_concept/(?P<pk>\d+)$', HighConceptFormView.as_view()),
	url(r'^create/trouble/(?P<pk>\d+)$', TroubleFormView.as_view()),
	url(r'^create/phases/(?P<pk>\d+)$', PhasesFormView.as_view()),
	url(r'^create/choose_skills/(?P<pk>\d+)$', ChooseSkillsFormView.as_view()),
	url(r'^create/powers_and_stunts/(?P<pk>\d+)$', PowersStuntsFormView.as_view()),
)
