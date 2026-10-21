from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('ejercicios/', views.ejercicios_view, name='ejercicios'),
    path('entrenamientos/', views.entrenamientos_view, name='entrenamientos'),
    path('equipos/', views.equipos_view, name='equipos'),
    path('espacios/', views.espacios_view, name='espacios'),
    path('informacion/', views.informacion_view, name='informacion'),
    path('ingresos/', views.ingresos_view, name='ingresos'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('mantenimiento/', views.mantenimiento_view, name='mantenimiento'),
    path('rutinas/', views.rutinas_view, name='rutinas'),
    path('usuarios/', views.usuarios_view, name='usuarios'),
    path('valoracion/', views.valoracion_view, name='valoracion'),
]