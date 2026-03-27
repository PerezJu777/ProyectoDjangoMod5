from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"medico", views.MedicoViewSet)
router.register(r"paciente", views.PacienteViewSet)
router.register(r"consulta", views.ConsultaViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("", include(router.urls)),
    path('recetas/',views.recetas_view),
]