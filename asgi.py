import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gimnasio.settings')

# 1. Cargar Django ASGI
django_app = get_asgi_application()

# 2. Instancia de FastAPI expuesta como 'app'
app = FastAPI(title="API Gimnasio")

@app.get("/fastapi/ping")
def ping():
    return {"status": "ok", "framework": "FastAPI"}

# 3. Montar Django en la raíz para servir el resto de vistas y admin
app.mount("/", django_app)