from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from Contratos.apps.authentication.models import User
from Contratos.apps.authentication.serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
