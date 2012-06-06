from django.db import models
from city.models import Aspect

class CharacterSheet(models.Model):
	name = models.CharField(max_length=200)
	template = models.ForeignKey('TemplateDescription')
	high_concept = models.CharField(max_length=75)
	trouble = models.CharField(max_length=75)
	background = models.CharField(max_length=200)
	risingconflict = models.CharField(max_length=200)
	the_story = models.TextField()
	guest_star = models.TextField()
	guest_star_redux = models.TextField()

class Skill(models.Model):
	name = models.CharField(max_length=200)

class SkillDescription( models.Model):
	name = models.CharField(max_length=200)

class TemplateDescription(models.Model):
	name = models.CharField(max_length=200)

