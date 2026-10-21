from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, 'FrontWeb/index.html')

def ejercicios_view(request):
    return render(request, 'FrontWeb/ejercicios.html')

def entrenamientos_view(request):
    return render(request, 'FrontWeb/entrenamientos.html')

def equipos_view(request):
    return render(request, 'FrontWeb/equipos.html')

def espacios_view(request):
    return render(request, 'FrontWeb/espacios.html')

def informacion_view(request):
    return render(request, 'FrontWeb/informacion.html')

def ingresos_view(request):
    return render(request, 'FrontWeb/ingresos.html')

def inventario_view(request):
    return render(request, 'FrontWeb/inventario.html')

def mantenimiento_view(request):
    return render(request, 'FrontWeb/mantenimiento.html')

def rutinas_view(request):
    return render(request, 'FrontWeb/rutinas.html')

def usuarios_view(request):
    return render(request, 'FrontWeb/usuarios.html')

def valoracion_view(request):
    return render(request, 'FrontWeb/valoracion.html')