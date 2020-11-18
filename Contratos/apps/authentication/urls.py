from django.urls import include, path
from rest_framework import routers
from Contratos.apps.authentication import views


router = routers.DefaultRouter()


router.register(r"useres", views.UserViewSet)


urlpatterns = [path("", include(router.urls))]
