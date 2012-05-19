from city_creation.models import Aspect, City, Concept
from django.contrib import admin

class ConceptInline(admin.StackedInline):
	model = Concept
	extra = 3

class CityAdmin(admin.ModelAdmin):
	inlines = [ConceptInline]

admin.site.register(City, CityAdmin)
admin.site.register(Aspect)
