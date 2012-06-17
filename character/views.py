from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView
from django.forms.models import inlineformset_factory
from character.models import *
from character.forms import *

class CharacterListView( ListView):
	model=CharacterSheet
	queryset = CharacterSheet.objects.all().order_by('-name')

class ChooseATemplateFormView (CreateView):
	form_class=ChooseATemplateForm
	model=CharacterSheet
	template_name='character/template_form.html'
	success_url='/character/create/choose_power_level/{0}'

	def form_valid( self, form):
		if form.is_valid():
			character_sheet= form.save()
		 	return HttpResponseRedirect(self.success_url.format(character_sheet.pk))
		else:
			return self.render_to_response(self.get_context_data(form=form))

class ChooseAPowerLevelFormView(UpdateView):
	form_class=ChooseAPowerLevelForm
	model=CharacterSheet
	success_url='/character/create/high_concept/{0}'
	def form_valid( self, form):
		if form.is_valid():
			self.object = form.save()
		 	return HttpResponseRedirect(self.success_url.format(self.object.pk))
		else:
			return self.render_to_response(self.get_context_data(form=form))

class HighConceptFormView(UpdateView):
	form_class=HighConceptForm
	model=CharacterSheet
	template_name='character/high_concept_form.html'
	success_url='/character/create/trouble/{0}'
	def form_valid( self, form):
		if form.is_valid():
			character_sheet= form.save()
		 	return HttpResponseRedirect(self.success_url.format(character_sheet.pk))
		else:
			return self.render_to_response(self.get_context_data(form=form))

class TroubleFormView(UpdateView):
	form_class=TroubleForm
	model=CharacterSheet
	template_name='character/trouble_form.html'
	success_url='/character/create/phases/{0}'
	def form_valid( self, form):
		if form.is_valid():
			character_sheet= form.save()
		 	return HttpResponseRedirect(self.success_url.format(character_sheet.pk))
		else:
			return self.render_to_response(self.get_context_data(form=form))

class PhasesFormView(UpdateView):
	form_class=PhasesForm
	model=CharacterSheet
	template_name='character/phases_form.html'
	success_url='/character/create/choose_skills/{0}'
	context_object_name='character_sheet_form'
	def form_valid( self, form):
		if form.is_valid():
			character_sheet= form.save(commit=False)
			self.add_aspect( form.cleaned_data['background_aspect'])
			self.add_aspect( form.cleaned_data['rising_conflict_aspect'])
			self.add_aspect( form.cleaned_data['the_story_aspect'])
			self.add_aspect( form.cleaned_data['guest_star_aspect'])
			self.add_aspect( form.cleaned_data['guest_star_redux_aspect'])
			character_sheet.save()
		 	return HttpResponseRedirect(self.success_url.format(character_sheet.pk))
		else:
			return self.render_to_response(self.get_context_data(form=form))

	def add_aspect(self, aspect_field):
			aspect =  Aspect( name=aspect_field)
			aspect.save()
			self.object.aspects.add(aspect)
		

class ChooseSkillsFormView(UpdateView):
	form_class=ChooseSkillsForm
	model=CharacterSheet
	template_name='character/choose_skills_form.html'
	success_url='/character/create/powers_and_stunts/{0}'

	def form_valid( self, form):
		character_sheet= form.save()
	 	return HttpResponseRedirect(self.success_url.format(character_sheet.pk))

	def get_context_data(self, **kwargs):
		SkillFormset = inlineformset_factory(CharacterSheet, Skill)
		context = super(ChooseSkillsFormView, self).get_context_data(**kwargs)
		context['inline_skills'] = SkillFormset(instance=self.object)
		context['power_level'] = self.object.power_level
		return context

class PowersStuntsFormView(UpdateView):
	form_class=PowerStuntsForm
	model=CharacterSheet
	template_name='character/powers_and_stunts.html'
	success_url='/character/{0}'
	def form_valid( self, form):
		if form.is_valid():
			character_sheet= form.save()
		 	return HttpResponseRedirect(self.success_url.format(character_sheet.pk))
		else:
			return self.render_to_response(self.get_context_data(form=form))


