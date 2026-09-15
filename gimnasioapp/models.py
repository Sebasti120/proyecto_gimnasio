from django.db import models
from django.contrib.auth.models import AbstractUser

class Gimnasio(models.Model):
    id_gimnasio = models.AutoField(primary_key=True)
    nombre_gym = models.CharField(max_length=150)
    ubicacion_gym = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_gym



class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección")
    
    # Opcional: Roles (Cliente, Entrenador, Administrador)
    ROL_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('FUNCIONARIO', 'Funcionario'),
        ('CLIENTE', 'Cliente'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='CLIENTE', verbose_name="Rol de Usuario")

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"




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
    # Dificultad de la rutina
    NIVEL_CHOICES = [
        ('PRINCIPIANTE', 'Principiante'),
        ('INTERMEDIO', 'Intermedio'),
        ('AVANZADO', 'Avanzado'),
    ]

    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Rutina")
    descripcion = models.TextField(verbose_name="Descripción detallada")
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES, default='PRINCIPIANTE', verbose_name="Nivel")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def __str__(self):
        return f"{self.nombre} ({self.nivel})"

    class Meta:
        verbose_name = "Rutina"
        verbose_name_plural = "Rutinas"
        ordering = ['nombre']




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


class Meta:
    verbose_name = "Usuario"
    verbose_name_plural = "Usuarios"

        
class ValoracionFisica(models.Model):
    id_valoracion = models.AutoField(primary_key=True)
    regularidad_fisica = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=100)
    disponibilidad = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def clean(self):
        errores = {}
        for campo, mensaje in {
            'regularidad_fisica': 'La regularidad física no puede estar vacía.',
            'objetivo': 'El objetivo no puede estar vacío.',
            'disponibilidad': 'La disponibilidad no puede estar vacía.',
        }.items():
            valor = getattr(self, campo)
            if not valor or not valor.strip():
                errores[campo] = mensaje


    def mostrar_informacion(self):
        return {
            'id_valoracion': self.id_valoracion,
            'regularidad_fisica': self.regularidad_fisica,
            'objetivo': self.objetivo,
            'disponibilidad': self.disponibilidad,
            'activo': self.activo,
        }

    def eliminar(self):
        self.activo = False


class RegistroEjercicio(models.Model):
    id_ejercicio = models.AutoField(primary_key=True)
    nombre_ejercicio = models.CharField(max_length=100)
    grupo_muscular = models.CharField(max_length=100)
    tipo_ejercicio = models.CharField(max_length=100)
    descripcion_tecnica = models.TextField()
    contraindicaciones = models.TextField()
    activo = models.BooleanField(default=True)

    def clean(self):
        errores = {}
        for campo, mensaje in {
            'nombre_ejercicio': 'El nombre del ejercicio no puede estar vacío.',
            'grupo_muscular': 'El grupo muscular no puede estar vacío.',
            'tipo_ejercicio': 'El tipo de ejercicio no puede estar vacío.',
            'descripcion_tecnica': 'La descripción técnica no puede estar vacía.',
            'contraindicaciones': 'Las contraindicaciones no pueden estar vacías.',
        }.items():
            valor = getattr(self, campo)
            if not valor or not valor.strip():
                errores[campo] = mensaje

    def mostrar_informacion(self):
        return {
            'id_ejercicio': self.id_ejercicio,
            'nombre_ejercicio': self.nombre_ejercicio,
            'grupo_muscular': self.grupo_muscular,
            'tipo_ejercicio': self.tipo_ejercicio,
            'descripcion_tecnica': self.descripcion_tecnica,
            'contraindicaciones': self.contraindicaciones,
            'activo': self.activo,
        }

    def eliminar(self):
        self.activo = False