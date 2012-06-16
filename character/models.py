from django.db import models
from core.models import Aspect, SkillDescription, Template

class CharacterSheet(models.Model):
	name = models.CharField(max_length=200)
	template = models.ForeignKey(Template)
	high_concept = models.CharField(max_length=75)
	trouble = models.CharField(max_length=75)
	background = models.TextField()
	musts = models.TextField()
	rising_conflict = models.TextField()
	the_story = models.TextField()
	guest_star = models.TextField()
	guest_star_redux = models.TextField()
	def __unicode__(self):
		return self.name

class Skill(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

