from rest_framework import serializers
from Contratos.apps.personas.models import Persona, Supervisor, Contratista


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = [field.name for field in Persona._meta.fields]


class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = [field.name for field in Supervisor._meta.fields]


class ContratistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contratista
        fields = [field.name for field in Contratista._meta.fields]
