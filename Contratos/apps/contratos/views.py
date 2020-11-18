from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from Contratos.apps.contratos.models import Contrato, Seguimiento, Producto
from Contratos.apps.contratos.serializers import (
    ContratoSerializer,
    SeguimientoSerializer,
    ProductoSerializer,
)

# Create your views here.


class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    permission_classes = [permissions.AllowAny]


class SeguimientoViewSet(viewsets.ModelViewSet):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer
    permission_classes = [permissions.AllowAny]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]
