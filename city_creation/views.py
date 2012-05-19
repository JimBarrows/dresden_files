# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

def index( request):
	return render_to_response( 'city/create/index.html', {}, context_instance=RequestContext(request))
