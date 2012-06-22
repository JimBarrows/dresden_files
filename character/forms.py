from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory, inlineformset_factory
from django import forms
from django.contrib.formtools.wizard.views import SessionWizardView
from character.models import *

class ChooseATemplateForm( ModelForm):
	class Meta:
		model = CharacterSheet
		fields=['template']

class ChooseAPowerLevelForm( ModelForm):
	class Meta:
		model = CharacterSheet
		fields=['power_level']

class HighConceptForm( ModelForm):
	class Meta:
		model = CharacterSheet
		fields=['high_concept']

class TroubleForm( ModelForm):
	class Meta:
		model = CharacterSheet
		fields=['trouble']

class PhasesForm( ModelForm):
	background_aspect = forms.CharField()
	rising_conflict_aspect = forms.CharField()
	the_story_aspect = forms.CharField()
	guest_star_aspect = forms.CharField()
	guest_star_redux_aspect = forms.CharField()
	class Meta:
		model = CharacterSheet
		fields=['background', 'rising_conflict', 'the_story', 'guest_star', 'guest_star_redux']

class ChooseSkillsForm( ModelForm):
	superb_skills = forms.MultipleChoiceField()
	great_skills = forms.MultipleChoiceField()
	good_skills = forms.MultipleChoiceField()
	fair_skills = forms.MultipleChoiceField()
	average_skills = forms.MultipleChoiceField()
	class Meta:
		model = CharacterSheet
		fields=['name', 'template', 'power_level']

class PowerStuntsForm( ModelForm):
	class Meta:
		model = CharacterSheet
		fields=['powers', 'stunts']
