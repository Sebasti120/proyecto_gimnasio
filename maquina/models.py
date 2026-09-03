from django.db import models

# Create your models here.
class Mantenimiento(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    descripcion_problema = models.TextField()
    fecha_reporte = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"Mantenimiento de {self.equipo.nombre} - {self.estado}"
