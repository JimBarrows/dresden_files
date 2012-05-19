from city.models import Aspect, City, Concept, Face, FaceRelationship
from django.contrib import admin

class ConceptInline(admin.StackedInline):
	model = Concept
	extra = 3

class FaceRelationshipInline(admin.StackedInline):
	model=FaceRelationship
	fk_name = 'to_face'
	extra = 1

class CityAdmin(admin.ModelAdmin):
	inlines = [ConceptInline]

class FaceAdmin(admin.ModelAdmin):
	inlines = [FaceRelationshipInline]

admin.site.register(Aspect)
admin.site.register(City, CityAdmin)
admin.site.register(Face, FaceAdmin)
