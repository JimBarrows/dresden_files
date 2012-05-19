from django.db import models

THEME_OR_THREAT_CHOICES=(
	('TE', 'Theme'),
	('TR', 'Threat'),
)

class City(models.Model):
	name = models.CharField(max_length=200)
	campaign_title = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class Concept(models.Model):
	city = models.ForeignKey(City)
	theme = models.CharField(max_length=2, choices=THEME_OR_THREAT_CHOICES)
	idea = models.CharField(max_length=200)

class Aspect(models.Model):
	name = models.CharField(max_length=200)
	city = models.ForeignKey(City)
	
