from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory, inlineformset_factory
from django import forms
from django.contrib.formtools.wizard.views import SessionWizardView
from character.models import *

class CharacterSheetForm( ModelForm):
	class Meta:
		model = CharacterSheet

