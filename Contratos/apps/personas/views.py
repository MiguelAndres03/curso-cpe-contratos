from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from Contratos.apps.personas.models import Persona, Supervisor, Contratista
from Contratos.apps.personas.serializers import (
    PersonaSerializer,
    SupervisorSerializer,
    ContratistaSerializer,
)

# Create your views here.


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.AllowAny]


class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer
    permission_classes = [permissions.AllowAny]


class ContratistaViewSet(viewsets.ModelViewSet):
    queryset = Contratista.objects.all()
    serializer_class = ContratistaSerializer
    permission_classes = [permissions.AllowAny]
