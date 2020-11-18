from django.contrib import admin
from Contratos.apps.contratos.models import Contrato, Seguimiento, Producto

# Register your models here.


class ContratoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contrato._meta.fields]


class SeguimientoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Seguimiento._meta.fields]


class ProductoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Producto._meta.fields]


admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Seguimiento, SeguimientoAdmin)
admin.site.register(Producto, ProductoAdmin)
