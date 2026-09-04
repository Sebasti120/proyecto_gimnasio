from django.shortcuts import render
from .models import Equipo
from .models import Mantenimiento

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'maquina/lista_equipos.html', {'equipos': equipos})


def historial_mantenimiento(request):
    mantenimientos = Mantenimiento.objects.select_related('equipo').all().order_by('-fecha_mantenimiento')
    return render(request, 'maquina/historial_mantenimiento.html', {'mantenimientos': mantenimientos})