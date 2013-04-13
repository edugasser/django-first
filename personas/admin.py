from django.contrib import admin
from personas.models import Ficha_Persona,Congregacion,Info_Extra,Tipo_Info_Extra,Grupo,Lugar_Reunion,Tipo_Grupo

class FichaPersonaAdmin(admin.ModelAdmin):
	pass
admin.site.register(Ficha_Persona,FichaPersonaAdmin) 

class InfoExtraAdmin(admin.ModelAdmin):
	pass
admin.site.register(Info_Extra,InfoExtraAdmin) 

class TipoInfoExtraAdmin(admin.ModelAdmin):
	pass
admin.site.register(Tipo_Info_Extra,TipoInfoExtraAdmin) 

class GrupoAdmin(admin.ModelAdmin):
	exclude = ('update_anfitrion_at','visibilidad')
admin.site.register(Grupo,GrupoAdmin) 

class Tipo_GrupoAdmin(admin.ModelAdmin):
	pass
admin.site.register(Tipo_Grupo,Tipo_GrupoAdmin) 

class Lugar_ReunionAdmin(admin.ModelAdmin):
	pass
admin.site.register(Lugar_Reunion,Lugar_ReunionAdmin) 

class CongregacionAdmin(admin.ModelAdmin):
	pass
admin.site.register(Congregacion,CongregacionAdmin) 

