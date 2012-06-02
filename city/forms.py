from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django import forms
from django.contrib.formtools.wizard.views import SessionWizardView
from city.models import THEME_OR_THREAT_CHOICES, City, ThemeThreat, Aspect, Face, Location


"""City Creation:
	1) Choose your city (Page 26)
	1.1) Themes/Threats
	2) Locations ( Page 37)
	3) Creat PCs ( Page 45)
	4) Finish up ( Page 46)"""

class CityForm( ModelForm):
	"""The core fields for a city, for use in a wizard"""
	class Meta:
		model = City

class ThemeThreatForm( ModelForm):
	"""The core fields for a theme or threat, for use in a wizard"""
	class Meta:
		model = ThemeThreat
		exclude = ('city',)

class AspectForm( ModelForm):
	class Meta:
		model = Aspect

class FaceForm( ModelForm):
	"""The faces section of a concept are only a name and a concept, so that's all we need."""
	class Meta:
		model = Face
		fields = ('name', 'high_concept', 'motivation', )

class LocationForm( ModelForm):
	class Meta:
		model = Location
		fields = ('name', 'description', 'theme_or_threat', 'idea',)

ThemeThreatFormSet = modelformset_factory(ThemeThreat)
AspectFormSet = modelformset_factory(Aspect)
FaceFormSet = modelformset_factory( Face)
LocationFormSet = modelformset_factory( Location)
