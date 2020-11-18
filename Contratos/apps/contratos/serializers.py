from rest_framework import serializers
from Contratos.apps.contratos.models import Contrato, Seguimiento, Producto


class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = [field.name for field in Contrato._meta.fields]


class SeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento
        fields = [field.name for field in Seguimiento._meta.fields]


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [field.name for field in Producto._meta.fields]
