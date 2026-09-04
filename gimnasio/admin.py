from django.contrib import admin
from .models import Ejercicio, Rutina, DetalleRutina

class DetalleRutinaInline(admin.TabularInline):
    model = DetalleRutina
    extra = 1

admin.site.register(Ejercicio)
admin.site.register(DetalleRutina)