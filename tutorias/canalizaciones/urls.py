from django.urls import path
from .views import SolicitudListView, SolicitudCreateView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SolicitudViewSet
from . import views

router = DefaultRouter()
router.register(r'solicitudes', SolicitudViewSet, basename='solicitud')

urlpatterns = [
    path('solicitudes/', SolicitudListView.as_view(), name='listar_solicitudes'),
    path('solicitudes/nueva/', SolicitudCreateView.as_view(), name='crear_solicitud'),
    path('', include(router.urls)),  # Incluir las URLs de la app
    path('registrar-alumno/', views.registrar_alumno, name='registrar_alumno'),
    path('listar-alumnos/', views.listar_alumnos, name='listar_alumnos'),
]
