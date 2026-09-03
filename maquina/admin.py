from django.contrib import admin
from .models import Mantenimiento, Equipo  

admin.site.register(Equipo)
admin.site.register(Mantenimiento)