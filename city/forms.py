from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django import forms
from django.contrib.formtools.wizard.views import SessionWizardView
from city.models import THEME_OR_THREAT_CHOICES


"""City Creation:
	1) Choose your city (Page 26)
	1.1) Themes/Threats
	2) Locations ( Page 37)
	3) Creat PCs ( Page 45)
	4) Finish up ( Page 46)"""

class ConceptFaceForm( forms.Form):
	"""The faces section of a concept are only a name and a concept, so that's all we need."""
	name=forms.CharField(max_length=75)
	concept=forms.CharField(max_length=200)

class ConceptForm( forms.Form):
	"""The core fields for a theme or threat, for use in a wizard"""
	theme=forms.ChoiceField(THEME_OR_THREAT_CHOICES,widget=forms.RadioSelect)
	idea = forms.CharField(max_length=200)
	aspect = forms.CharField(max_length=200)
	faces = formset_factory( ConceptFaceForm,extra=1)


class CityForm( forms.Form):
	"""The core fields for a city, for use in a wizard"""
	name = forms.CharField(max_length=200)
	campaign = forms.CharField(max_length=200)
	concepts = formset_factory( ConceptForm,extra=3, max_num=3)
	supernatural_status_quo = forms.CharField(max_length=200,widget=forms.Textarea)
	mundane_status_quo = forms.CharField(max_length=200,widget=forms.Textarea)




