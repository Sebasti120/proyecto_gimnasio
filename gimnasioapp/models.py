from django.db import models

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=120)
    grupo_muscular = models.CharField(max_length=80, blank=True)
    tipo = models.CharField(max_length=50, blank=True)
    descripcion_tecnica = models.TextField(blank=True)
    contraindicaciones = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='ejercicios/', blank=True, null=True)

    def __str__(self):
        return self.nombre