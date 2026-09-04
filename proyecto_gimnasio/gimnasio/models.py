from django.db import models
from django.contrib.auth.models import AbstractUser

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