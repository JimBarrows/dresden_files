from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import SessionWizardView
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from city.models import City, ThemeThreat, Aspect
from city.forms import CityForm,ThemeThreatForm

def index( request):
	city_list = City.objects.all().order_by('-name')
	return render_to_response( 'city/index.html', {'city_list' : city_list}, context_instance=RequestContext(request))

def view( request, city_id):
	c = get_object_or_404(City, pk=city_id)
	return render_to_response('city/view.html', {'city':c}, context_instance=RequestContext(request))

def create( request):
	return render_to_response('city/form.html', {'city_form':CityForm(),},context_instance=RequestContext(request))

def save( request):
	if request.method == 'POST' :
		city_form = CityForm(request.POST)
		if city_form.is_valid():
			city_form.save()
			return HttpResponseRedirect('/city/{0}'.format(city.pk))
		else:
			return render_to_response('city/form.html', {'city_form':city_form,},context_instance=RequestContext(request))

class CreateCityWizard(SessionWizardView):
	def done(self, form_list, **kwargs):
		return render_to_response('city/view.html', {}, context_instance=RequestContext(request))
