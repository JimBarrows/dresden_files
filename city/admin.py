from city.models import Aspect, City, ThemeThreat, Face, FaceRelationship, Location
from django.contrib import admin

class ThemeThreatInline(admin.StackedInline):
	model = ThemeThreat
	extra = 3

class FaceRelationshipInline(admin.StackedInline):
	model=FaceRelationship
	fk_name = 'to_face'
	extra = 1

class CityAdmin(admin.ModelAdmin):
	inlines = [ThemeThreatInline]

class FaceAdmin(admin.ModelAdmin):
	inlines = [FaceRelationshipInline]

#class LocationAdmin(admin.ModelAdmin):

admin.site.register(Aspect)
admin.site.register(City, CityAdmin)
admin.site.register(Face, FaceAdmin)
admin.site.register(Location) #, LocationAdmin)
