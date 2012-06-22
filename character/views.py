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
		self.object =form.save()
	 	return HttpResponseRedirect(self.success_url.format(self.object.pk))

class ChooseAPowerLevelFormView(UpdateView):
	form_class=ChooseAPowerLevelForm
	model=CharacterSheet
	success_url='/character/create/high_concept/{0}'
	def form_valid( self, form):
		self.object = form.save()
	 	return HttpResponseRedirect(self.success_url.format(self.object.pk))

class HighConceptFormView(UpdateView):
	form_class=HighConceptForm
	model=CharacterSheet
	template_name='character/high_concept_form.html'
	success_url='/character/create/trouble/{0}'
	def form_valid( self, form):
		self.object = form.save()
	 	return HttpResponseRedirect(self.success_url.format(self.object.pk))

class TroubleFormView(UpdateView):
	form_class=TroubleForm
	model=CharacterSheet
	template_name='character/trouble_form.html'
	success_url='/character/create/phases/{0}'
	def form_valid( self, form):
		self.object = form.save()
	 	return HttpResponseRedirect(self.success_url.format(self.object.pk))

class PhasesFormView(UpdateView):
	form_class=PhasesForm
	model=CharacterSheet
	template_name='character/phases_form.html'
	success_url='/character/create/choose_skills/{0}'
	def form_valid( self, form):
		self.add_aspect( form.cleaned_data['background_aspect'])
		self.add_aspect( form.cleaned_data['rising_conflict_aspect'])
		self.add_aspect( form.cleaned_data['the_story_aspect'])
		self.add_aspect( form.cleaned_data['guest_star_aspect'])
		self.add_aspect( form.cleaned_data['guest_star_redux_aspect'])
		self.object.save()
		return HttpResponseRedirect(self.success_url.format(self.object .pk))

	def add_aspect(self, aspect_field):
			aspect =  Aspect( name=aspect_field)
			aspect.save()
			self.object.aspects.add(aspect)
		

SkillFormset = inlineformset_factory(CharacterSheet, Skill)

class ChooseSkillsFormView(UpdateView):
	form_class=ChooseSkillsForm
	model=CharacterSheet
	template_name='character/choose_skills_form.html'
	success_url='/character/create/powers_and_stunts/{0}'

	def form_valid( self, form):
		context = self.get_context_data()
		skill_forms = context['inline_skills']
		if skill_forms.is_valid():
			print "skill_forms is valid"
			skill_forms.instance = self.object
			skill_forms.save()
			self.object = form.save()
		 	return HttpResponseRedirect(self.success_url.format(self.object .pk))
		else:
			return self.render_to_response(self.get_context_data(form=form))

	def get_context_data(self, **kwargs):
		context = super(ChooseSkillsFormView, self).get_context_data(**kwargs)
		if self.request.POST:
			context['inline_skills'] = SkillFormset(self.request.POST, instance=self.object)
		else:
			context['inline_skills'] = SkillFormset(instance=self.object)
		context['power_level'] = self.object.power_level
		return context

class PowersStuntsFormView(UpdateView):
	form_class=PowerStuntsForm
	model=CharacterSheet
	template_name='character/powers_and_stunts.html'
	success_url='/character/{0}'
	def form_valid( self, form):
		self.object = form.save()
	 	return HttpResponseRedirect(self.success_url.format(self.object .pk))


