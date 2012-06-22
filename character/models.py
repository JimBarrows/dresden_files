from django.db import models
from django.core.exceptions import ValidationError
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

#	def clean(self):
#		if self.pk:
#			number_of_superb = self.count_skills_at(5)
#			number_of_great = self.count_skills_at(4)
#			number_of_good = self.count_skills_at(3)
#			number_of_fair = self.count_skills_at(2)
#			number_of_average = self.count_skills_at(1)
#			print 'Superb: {0} Great: {1} Good: {2}'.format(number_of_superb, number_of_great, number_of_good)
#			if number_of_superb > number_of_great:
#				raise ValidationError('You cannot have more superb skills then great')
#			if number_of_great > number_of_fair:
#				raise ValidationError('You cannot have more great skills then fair')
#			if number_of_fair > number_of_average:
#				raise ValidationError('You cannot have more fair skills then average')

	def count_skills_at(self, skill_level):
		return Skill.objects.filter( character_sheet = self).filter( level = skill_level).count()

class Skill(models.Model):
	character_sheet = models.ForeignKey(CharacterSheet)
	skill_description = models.ForeignKey(SkillDescription)
	level = models.IntegerField(choices=The_Ladder)
	def __unicode__(self):
		return '{0} ({1})'.format(self.skill_description.name, self.level)

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
