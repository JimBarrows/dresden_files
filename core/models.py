from django.db import models
from city.models import ThemeThreat, Location, City

The_Ladder=(
	(8, 'Legendary'),
	(7, 'Epic'),
	(6, 'Fantastic'),
	(5, 'Superb'),
	(4, 'Great'),
	(3, 'Good'),
	(2, 'Fair'),
	(1, 'Average'),
	(0, 'Mediocre'),
	(-1, 'Poor'),
	(-2, 'Terrible'),
	)

Supernatural_Power_Categories=(
	('CF', 'Creature Feature'),
	('FM', 'Faerie Magic'),
	('IP', 'Items of Power'),
	('MA', 'Minor Ability'),
	('NP', 'Nevernever Power'),
	('PA', 'Psychic Ability'),
	('SD', 'Speed'),
	('SP', 'Spellcraft'),
	('SS', 'Shapeshifting'),
	('ST', 'Strength'),
	('TF', 'True Faith'),
	('TO', 'Toughness'),
	('VA', 'Vampirism'),
	)

class Template (models.Model):
	name = models.CharField(max_length=75)
	description = models.TextField()
	minimum_refresh = models.IntegerField()
	important_skills = models.ManyToManyField('SkillDescription', null=True, blank=True)
	def __unicode__(self):
		return self.name

class Must (models.Model):
	name = models.CharField(max_length=75)
	description = models.TextField()
	template = models.ForeignKey(Template)
	supernatural_power = models.ForeignKey('PowerDescription', null=True, blank=True)
	def __unicode__(self):
		return self.name

class TemplateOption (models.Model):
	name = models.CharField(max_length=75)
	description = models.TextField()
	template = models.ForeignKey(Template)
	def __unicode__(self):
		return self.name

class SkillDescription (models.Model):
	name = models.CharField(max_length=75)
	description = models.TextField()
	def __unicode__(self):
		return self.name

class TrappingDescription (models.Model):
	name = models.CharField(max_length=75)
	description = models.TextField()
	skill_description = models.ForeignKey(SkillDescription)
	def __unicode__(self):
		return self.name

class StuntDescription (models.Model):
	name = models.CharField(max_length=75)
	description = models.TextField()
	skill_description = models.ForeignKey(SkillDescription)
	def __unicode__(self):
		return self.name

class PowerDescription (models.Model):
	name = models.CharField(max_length=75)
	description = models.TextField()
	note = models.TextField(null=True, blank=True)
	cost = models.IntegerField()
	category =  models.CharField(max_length=2, choices=Supernatural_Power_Categories)
	skills_affected = models.ManyToManyField('SkillDescription', null=True, blank=True)
	def __unicode__(self):
		return self.name

class Effect (models.Model):
	name = models.CharField(max_length=75)
	description = models.TextField()
	power = models.ForeignKey(PowerDescription)
	def __unicode__(self):
		return self.name

class Aspect(models.Model):
	name = models.CharField(max_length=75)
	concept = models.ForeignKey(ThemeThreat, null=True, blank=True)
	location = models.ForeignKey(Location, null=True, blank=True)
	city = models.ForeignKey(City, null=True, blank=True)
	def __unicode__(self):
		return self.name

class PowerLevel(models.Model):
	name = models.CharField(max_length=75)
	refresh = models.IntegerField()
	skill_points = models.IntegerField()
	skill_cap =  models.IntegerField(choices=The_Ladder)
	def __unicode__(self):
		return self.name
