from django.urls import path
from .views import EquipoViewSet, MantenimientoViewSet

urlpatterns = [
    path('equipos/', EquipoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('equipos/<int:pk>/', EquipoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('mantenimientos/', MantenimientoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('mantenimientos/<int:pk>/', MantenimientoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]