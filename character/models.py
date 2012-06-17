from django.db import models
from core.models import Aspect, SkillDescription, Template, PowerLevel, The_Ladder, StuntDescription, PowerDescription

class CharacterSheet(models.Model):
	name = models.CharField(max_length=200)
	template = models.ForeignKey(Template)
	power_level = models.ForeignKey(PowerLevel, blank=True, null=True)
	high_concept = models.CharField(max_length=75)
	trouble = models.CharField(max_length=75)
	aspects = models.ManyToManyField(Aspect, blank=True, null=True)
	background = models.TextField()
	rising_conflict = models.TextField()
	the_story = models.TextField()
	guest_star = models.TextField()
	guest_star_redux = models.TextField()
	skills = models.ManyToManyField(SkillDescription, through='Skill', blank=True, null=True)
	stunts = models.ManyToManyField(StuntDescription, through='Stunt', blank=True, null=True)
	powers = models.ManyToManyField(PowerDescription, through='Power', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Skill(models.Model):
	character_sheet = models.ForeignKey(CharacterSheet)
	skill_description = models.ForeignKey(SkillDescription)
	level = models.IntegerField(choices=The_Ladder)
	def __unicode__(self):
		return '{0} ({1})'.format(skill_description.name, level)

class Stunt(models.Model):
	character_sheet = models.ForeignKey(CharacterSheet)
	stunt_description = models.ForeignKey(StuntDescription)
	def __unicode__(self):
		return stunt_description.name

class Power(models.Model):
	character_sheet = models.ForeignKey(CharacterSheet)
	power_description = models.ForeignKey(PowerDescription)
	def __unicode__(self):
		return power_description.name
