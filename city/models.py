from django.db import models

THEME_OR_THREAT_CHOICES=(
	('TE', 'Theme'),
	('TR', 'Threat'),
)

class City(models.Model):
	name = models.CharField(max_length=200)
	campaign_title = models.CharField(max_length=200)
	supernatural_status_quo = models.TextField()
	mundane_status_quo = models.TextField()
	def __unicode__(self):
		return self.name

class Concept(models.Model):
	city = models.ForeignKey(City)
	theme = models.CharField(max_length=2, choices=THEME_OR_THREAT_CHOICES)
	idea = models.CharField(max_length=200)
	def __unicode__(self):
		return self.idea

class Aspect(models.Model):
	name = models.CharField(max_length=75)
	concept = models.ForeignKey(Concept, null=True, blank=True)
	location = models.ForeignKey('Location', null=True, blank=True)
	def __unicode__(self):
		return self.name

class Face(models.Model):
	name = models.CharField(max_length=200)
	high_concept = models.CharField(max_length=200)
	motivation = models.CharField(max_length=200)
	relationships = models.ManyToManyField('Face', through="FaceRelationship")
	concept = models.ForeignKey(Concept, null=True, blank=True)
	location = models.ForeignKey('Location', null=True, blank=True)
	def __unicode__(self):
		return self.name

class FaceRelationship(models.Model):
	name = models.CharField(max_length=200)
	from_face = models.ForeignKey('Face', related_name='from_face')
	to_face = models.ForeignKey('Face', related_name='to_face')
	def __unicode__(self):
		return self.name

class Location(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	theme = models.CharField(max_length=2, choices=THEME_OR_THREAT_CHOICES)
	idea = models.CharField(max_length=200)
	city = models.ForeignKey('City')
	def __unicode__(self):
		return self.name
