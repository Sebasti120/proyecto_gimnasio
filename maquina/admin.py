from django.contrib import admin
from .models import Mantenimiento

# Register your models here.


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id_equipo', 'marca', 'categoria', 'ubicacion', 'estado', 'numero_serie')
    list_filter = ('estado', 'categoria', 'ubicacion')
    search_fields = ('marca', 'numero_serie', 'categoria')

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'fecha_reporte', 'estado', 'descripcion_problema')
    list_filter = ('estado', 'fecha_reporte')
    search_fields = ('equipo__marca', 'equipo__numero_serie', 'descripcion_problema')
