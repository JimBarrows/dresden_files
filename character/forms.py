from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory, inlineformset_factory
from django import forms
from django.contrib.formtools.wizard.views import SessionWizardView
from character.models import *

class CharacterSheetForm( ModelForm):
	background_aspect = forms.CharField()
	rising_conflict_aspect = forms.CharField()
	the_story_aspect = forms.CharField()
	guest_star_aspect = forms.CharField()
	redux_aspect = forms.CharField()
	class Meta:
		model = CharacterSheet

