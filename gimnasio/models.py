from django.db import models

class rutina (models.model) :
    id_rutina: models.AutoField (primary_key=True)
    categoria: models.
    nombre_rutina: models.CharField (max_length=50)
    
class DetalleRutina(models.Model):
    id_detalle_rutina = models.AutoField(primary_key=True)
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name='detalles')
    id_ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='detalles_rutina')
    orden_ejercicio = models.CharField(max_length=50, blank=True, null=True)
    series_asignadas = models.IntegerField(default=0)
    repeticiones_asignadas = models.IntegerField(default=0)
    carga_asignada = models.CharField(max_length=50, blank=True, null=True)
    tiempo_descanso = models.CharField(max_length=50, blank=True, null=True)
    lado = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Detalle Rutina {self.id_rutina_id} - Ejercicio {self.id_ejercicio_id}"


class SesionEntrenamiento(models.Model):
    class EstadoSesion(models.TextChoices):
        PLANIFICADA = 'planificada', 'Planificada'
        EN_PROGRESO = 'en_progreso', 'En Progreso'
        COMPLETADA = 'completada', 'Completada'
        CANCELADA = 'cancelada', 'Cancelada'

    id_sesion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(
        max_length=20,
        choices=EstadoSesion.choices,
        default=EstadoSesion.PLANIFICADA
    )

    def __str__(self):
        return f"Sesión {self.id_sesion} - {self.get_estado_display()}"