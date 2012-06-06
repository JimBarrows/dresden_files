from django.db import models
#from dresden_files.city import models 

LADDER_CHOICES=(
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

#class Aspect(models.Model):
#	name = models.CharField(max_length=75)
#	concept = models.ForeignKey('dresden_files.city.models.ThemeThreat', null=True, blank=True)
#	location = models.ForeignKey('Location', null=True, blank=True)
#	city = models.ForeignKey('City', null=True, blank=True)
#	def __unicode__(self):
#		return self.name

