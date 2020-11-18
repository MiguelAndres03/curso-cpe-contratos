from django.urls import include, path
from rest_framework import routers
from Contratos.apps.personas import views


router = routers.DefaultRouter()


router.register(r"personas", views.PersonaViewSet)
router.register(r"supervisores", views.SupervisorViewSet)
router.register(r"contratistas", views.ContratistaViewSet)


urlpatterns = [path("", include(router.urls))]
