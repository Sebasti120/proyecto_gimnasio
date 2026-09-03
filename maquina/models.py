from django.db import models

# Create your models here.
class Mantenimiento(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    descripcion_problema = models.TextField()
    fecha_reporte = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"Mantenimiento de {self.equipo.nombre} - {self.estado}"
    
class CondicionMedica(models.Model):
    nombre = models.CharField(max_length=100)  # Ej: "Asma", "Lesión de rodilla", "Hipertensión"
    descripcion = models.TextField(blank=True, null=True) # Detalles o recomendaciones especiales
    requiere_autorizacion = models.BooleanField(default=False) # Si necesita aval médico para entrenar

    def __str__(self):
        return self.nombre