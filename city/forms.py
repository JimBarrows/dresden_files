from django.forms import ModelForm
from django import forms
from city.models import THEME_OR_THREAT_CHOICES
"""City Creation:
	1) Choose your city (Page 26)
	1.1) Themes/Threats
	2) Locations ( Page 37)
	3) Creat PCs ( Page 45)
	4) Finish up ( Page 46)"""
class CityForm( forms.Form):
	"""The core fields for a city, for use in a wizard"""
	name = forms.CharField(max_length=200)
	campaign_title = forms.CharField(max_length=200)

class ConceptForm( forms.Form):
	"""The core fields for a theme or threat, for use in a wizard"""
	theme=forms.ChoiceField(THEME_OR_THREAT_CHOICES)
	idea = forms.CharField(max_length=200)

class AspectForm( forms.Form):
	"""The core fields for an aspect, for use in a wizard"""
	name=forms.CharField(max_length=75)

class FaceForm( forms.Form):
	"""The core fields for a face, for use in a wizard"""
	name=forms.CharField(max_length=75)
	high_concept=forms.CharField(max_length=200)
	motivation=forms.CharField(max_length=200)

class LocationForm( forms.Form):
	"""The core fields for a form, for use in a wizard"""
	name=forms.CharField(max_length=200)
	description=forms.CharField(max_length=200)
	theme=forms.ChoiceField(THEME_OR_THREAT_CHOICES)
	idea=forms.CharField(max_length=200)

