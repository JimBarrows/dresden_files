from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import SessionWizardView
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from city.models import City, Concept

def index( request):
	city_list = City.objects.all().order_by('-name')[:5]
	return render_to_response( 'city/index.html', {'city_list' : city_list}, context_instance=RequestContext(request))

def view( request, city_id):
	c = get_object_or_404(City, pk=city_id)
	return render_to_response('city/view.html', {'city':c}, context_instance=RequestContext(request))

class CreateCityWizardView(SessionWizardView):
	def done( self, form_list, **kwargs):
		city = City()
		for form in form_list:
			if form.__class__.__name__ == 'CityForm':
				city.name = form.cleaned_data['name']
				city.campaign_title = form.cleaned_data['campaign_title']
				city.save()
			elif form.__class__.__name__ == 'ConceptForm':
				concept = Concept()
				concept.city = city
				concept.theme = form.cleaned_data['theme']
				concept.idea = form.cleaned_data['idea']
				city.concept_set.add( concept)
		city.save()
		return  HttpResponseRedirect('/city/{0}'.format(city.id))
