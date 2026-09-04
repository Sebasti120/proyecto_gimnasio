from django.db import models

class Gimnasio(models.Model):
    id_gimnasio = models.AutoField(primary_key=True)
    nombre_gym = models.CharField(max_length=150)
    ubicacion_gym = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_gym


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Ejercicio(models.Model):
    id_ejercicio = models.AutoField(primary_key=True)
    nombre_ejercicio = models.CharField(max_length=100)
    grupo_muscular = models.CharField(max_length=100)
    tipo_ejercicio = models.CharField(max_length=100)
    descripcion_tecnica = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_ejercicio


class Rutina(models.Model):
    id_rutina = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='rutinas')
    id_instructor = models.IntegerField(blank=True, null=True)
    nombre_rutina = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    frecuencia_semanal = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre_rutina} - {self.id_usuario.nombre}"


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
        return f"Detalle {self.id_detalle_rutina} - Rutina {self.id_rutina_id}"


class SesionEntrenamiento(models.Model):
    class EstadoSesion(models.TextChoices):
        PLANIFICADA = 'planificada', 'Planificada'
        EN_PROGRESO = 'en_progreso', 'En Progreso'
        COMPLETADA = 'completada', 'Completada'
        CANCELADA = 'cancelada', 'Cancelada'

    id_sesion = models.AutoField(primary_key=True)
    id_rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name='sesiones', null=True, blank=True)
    fecha = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=EstadoSesion.choices,
        default=EstadoSesion.PLANIFICADA
    )

    def __str__(self):
        return f"Sesion {self.id_sesion} ({self.get_estado_display()})"