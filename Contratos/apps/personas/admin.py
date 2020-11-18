from django.contrib import admin
from Contratos.apps.personas.models import Persona, Supervisor, Contratista

# Register your models here.


class PersonaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Persona._meta.fields]


class SupervisorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Supervisor._meta.fields]


class ContratistaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contratista._meta.fields]


admin.site.register(Persona, PersonaAdmin)
admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(Contratista, ContratistaAdmin)
