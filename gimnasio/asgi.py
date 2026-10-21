import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gimnasio.settings')

# 1. Cargar Django ASGI
django_app = get_asgi_application()

#Importaciones necesarias
from maquina.models import Equipo

# 2. Instancia de FastAPI expuesta como 'app'
app = FastAPI(title="API Gimnasio")

@app.get("/fastapi/ping")
def ping():
    return {"status": "ok", "framework": "FastAPI"}

@app.get("/maquina")
def get_maquina():
    return {
        "id": 2,
        "nombre": "Bicicleta estatica",
        "marca": "N-Man",
        "ubicacion": "Quebrajacho",
        "categoria": "Pierna",
        "numero de serie": "12456",
        "estado_equipo": "Buen estado"
    }

@app.get("/maquina/{maquina_id_equipo}")
def get_maquina(maquina_id_equipo: int):
    equipo = Equipo.objects.filter(id_equipo=maquina_id_equipo).first()
    if not equipo:
        return {"error": "No se encontró ningún equipo con ese ID"}

    
    return {
        "id_equipo": equipo.id_equipo,
        "nombre": equipo.nombre,
        "marca": equipo.marca,
        "ubicacion": equipo.ubicacion,
        "categoria": equipo.categoria,
        "numero_serie": equipo.numero_serie,
        "estado_equipo": equipo.estado_equipo
    }

@app.post("/maquina", status_code=201)
def crear_maquina(
    nombre: str, 
    marca: str, 
    ubicacion: str, 
    categoria: str, 
    numero_serie: str, 
    estado_equipo: str
):
    nuevo_equipo = Equipo.objects.create(
        nombre=nombre,
        marca=marca,
        ubicacion=ubicacion,
        categoria=categoria,
        numero_serie=numero_serie,
        estado_equipo=estado_equipo
    )
    return {"mensaje": "Equipo creado con éxito", "id": nuevo_equipo.id_equipo}


# 3. Montar Django en la raíz para servir el resto de vistas y admin
app.mount("/", django_app)