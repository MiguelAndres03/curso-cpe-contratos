from rest_framework import serializers
from Contratos.apps.authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [field.name for field in User._meta.fields]
