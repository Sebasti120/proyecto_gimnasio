from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id_equipo', 'categoria', 'marca', 'ubicacion', 'numero_serie', 'estado', 'id_gimnasio')
    list_filter = ('categoria', 'estado')
    search_fields = ('marca', 'numero_serie', 'categoria')

# Register your models here.

admin.site.register(Mantenimiento)
