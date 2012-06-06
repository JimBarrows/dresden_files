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
	character_sheet = CharacterSheet()
	character_sheet_form = CharacterSheetForm(instance=character_sheet)
	if request.method == "POST":
		character_sheet_form = CharacterSheetForm(request.POST,instance=character_sheet)
		if character_sheet_form.is_valid():
			character_sheet = character_sheet_form.save()
			return HttpResponseRedirect('/character/{0}'.format(character_sheet.id))
	return render_to_response( 'character/form.html', {'character_sheet_form' : character_sheet_form}, context_instance=RequestContext(request))

def view( request, character_id):
	character_sheet = get_object_or_404( CharacterSheet, pk=character_id)
	return render_to_response( 'character/view.html', {'character_sheet' : character_sheet}, context_instance=RequestContext(request))
	
def minor_milestone(request, character_id=None):
	character_list = CharacterSheet.objects.all().order_by('-name')
	return render_to_response( 'character/index.html', {'character_list' : character_list}, context_instance=RequestContext(request))

def significant_milestone(request, character_id=None):
	character_list = CharacterSheet.objects.all().order_by('-name')
	return render_to_response( 'character/index.html', {'character_list' : character_list}, context_instance=RequestContext(request))

def major_milestone(request, character_id=None):
	character_list = CharacterSheet.objects.all().order_by('-name')
	return render_to_response( 'character/index.html', {'character_list' : character_list}, context_instance=RequestContext(request))
