from django.contrib import admin

from .models import RegistroEjercicio, Rutina, ValoracionFisica


admin.site.register(Rutina)
admin.site.register(ValoracionFisica)
admin.site.register(RegistroEjercicio)
