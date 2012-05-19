# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from city.models import City

def index( request):
	city_list = City.objects.all().order_by('-name')[:5]
	return render_to_response( 'city/index.html', {'city_list' : city_list}, context_instance=RequestContext(request))

def view( request, city_id):
	c = get_object_or_404(City, pk=city_id)
	return render_to_response('city/view.html', {'city':c}, context_instance=RequestContext(request))
