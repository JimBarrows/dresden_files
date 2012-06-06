from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import SessionWizardView
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from character.models import *
from character.forms import *

def index( request):
	character_list = CharacterSheet.objects.all().order_by('-name')
	return render_to_response( 'character/index.html', {'character_list' : character_list}, context_instance=RequestContext(request))

def character_form(request, character_id=None):
	character_list = CharacterSheet.objects.all().order_by('-name')
	return render_to_response( 'character/index.html', {'character_list' : character_list}, context_instance=RequestContext(request))

def minor_milestone(request, character_id=None):
	character_list = CharacterSheet.objects.all().order_by('-name')
	return render_to_response( 'character/index.html', {'character_list' : character_list}, context_instance=RequestContext(request))

def significant_milestone(request, character_id=None):
	character_list = CharacterSheet.objects.all().order_by('-name')
	return render_to_response( 'character/index.html', {'character_list' : character_list}, context_instance=RequestContext(request))

def major_milestone(request, character_id=None):
	character_list = CharacterSheet.objects.all().order_by('-name')
	return render_to_response( 'character/index.html', {'character_list' : character_list}, context_instance=RequestContext(request))
