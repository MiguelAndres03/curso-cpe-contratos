from django.urls import include, path
from rest_framework import routers
from Contratos.apps.contratos import views


router = routers.DefaultRouter()


router.register(r"contratos", views.ContratoViewSet)
router.register(r"seguimientos", views.SeguimientoViewSet)
router.register(r"productos", views.ProductoViewSet)


urlpatterns = [path("", include(router.urls))]
