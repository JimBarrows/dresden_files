from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import SessionWizardView
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from city.models import City, ThemeThreat, Aspect
from city.forms import *

def index( request):
	city_list = City.objects.all().order_by('-name')
	return render_to_response( 'city/index.html', {'city_list' : city_list}, context_instance=RequestContext(request))

def view( request, city_id):
	c = get_object_or_404(City, pk=city_id)
	return render_to_response('city/view.html', {'city':c}, context_instance=RequestContext(request))

def faces( request, city_id):
	city = get_object_or_404(City, pk=city_id)
	faces_inline_formset = CityFacesInlineFormset( instance=city)
	return render_to_response('city/faces.html', 
		{'city':city,
		'faces':faces_inline_formset,}, 
		context_instance=RequestContext(request))

def theme_or_threat( request, city_id, theme_threat_id=None):

	city = get_object_or_404(City, pk=city_id)

	if theme_threat_id == None:
		theme_threat = ThemeThreat(city=city)
	else:
		theme_threat = ThemeThreat.objects.get(id = theme_threat_id)
		
	if request.method == "POST":
		theme_threat_form = ThemeThreatForm( request.POST, instance=theme_threat)
		faces_formset = ThemeOrThreatFacesInlineFormset( request.POST, instance=theme_threat)
		aspect_formset = ThemeOrThreatAspectInlineFormset( request.POST, instance=theme_threat)
		if theme_threat_form.is_valid() and faces_formset.is_valid() and aspect_formset.is_valid(): 
			theme_threat_form.save()
			faces_formset.save()
			aspect_formset.save()
			return HttpResponseRedirect('/city/{0}'.format(city_id))
	else:
		theme_threat_form = ThemeThreatForm(instance=theme_threat)
		faces_formset = ThemeOrThreatFacesInlineFormset(instance=theme_threat)
		aspect_formset = ThemeOrThreatAspectInlineFormset(instance=theme_threat)

	return render_to_response( 'city/theme_or_threat_form.html', 
		{'theme_or_threat_form' : theme_threat_form,
		 'faces_formset' : faces_formset,
		 'aspect_formset' : aspect_formset,
		 }, 
		context_instance=RequestContext(request))
	
def city_form( request):
	if request.method == "POST":
		city_form = CityForm( request.POST)
		if( city_form.is_valid()) :
			city = city_form.save()
			return HttpResponseRedirect('/city/{0}'.format(city.id))
	else :
		city_form = CityForm()
	return render_to_response( 'city/form.html', 
		{ 'city_form': city_form,},
		context_instance=RequestContext(request))
	

class CreateCityWizard(SessionWizardView):
	def done(self, form_list, **kwargs):
		return render_to_response('city/view.html', {})
