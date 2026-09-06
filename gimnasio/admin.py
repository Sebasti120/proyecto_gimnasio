from django.contrib import admin
from .models import Gimnasio, Usuario, Ejercicio, Rutina, DetalleRutina, SesionEntrenamiento

admin.site.register(Gimnasio)
admin.site.register(Usuario)
admin.site.register(Ejercicio)
admin.site.register(Rutina)
admin.site.register(DetalleRutina)
admin.site.register(SesionEntrenamiento)
