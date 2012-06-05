from city.models import *
from django.contrib import admin

class ThemeThreatInline(admin.StackedInline):
	model = ThemeThreat
	extra = 3


class CityAdmin(admin.ModelAdmin):
	inlines = [ThemeThreatInline]

admin.site.register(Aspect)
admin.site.register(City, CityAdmin)
admin.site.register(Face)
admin.site.register(Location)
