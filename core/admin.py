from models import *
from django.contrib import admin


class MustInline( admin.TabularInline):
	model=Must
	extra = 1

class TemplateOptionInline( admin.TabularInline):
	model=TemplateOption
	extra = 1

class TrappingDescriptionInline( admin.TabularInline):
	model=TrappingDescription
	extra = 1

class EffectInline( admin.TabularInline):
	model=Effect
	extra = 1

class TemplateAdmin( admin.ModelAdmin):
	inlines=[MustInline, TemplateOptionInline]

class SkillDescriptionAdmin( admin.ModelAdmin):
	inlines=[TrappingDescriptionInline]

class PowerDescriptionAdmin( admin.ModelAdmin):
	inlines=[EffectInline, MustInline]

admin.site.register( Template, TemplateAdmin)
admin.site.register( SkillDescription, SkillDescriptionAdmin)
admin.site.register( StuntDescription)
admin.site.register( PowerDescription, PowerDescriptionAdmin)
admin.site.register( PowerLevel)
