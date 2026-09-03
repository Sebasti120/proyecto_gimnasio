from django.db import models
# Create your models here.

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=100 defaul='' )
    marca = models.CharField(max_length=100 defaul='')
    ubicacion = models.CharField(max_length=150 defaul='')
    id_gimnasio = models.IntegerField()
    numero_serie = models.CharField(max_length=100, unique=True defaul='')
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.marca} - {self.categoria} ({self.numero_serie})"

#-----------Definicion de la enumeracion de estados----------------#

class Sesion(models.Model):

    class EstadoSesion(models.TextChoices):
        PROGRAMADA = 'PROGRAMADA', 'Programada'
        EN_PROCESO = 'EN_PROCESO', 'En Proceso'
        COMPLETADA = 'COMPLETADA', 'Completada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    # Campos del modelo
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    
    # Campo que utiliza la enumeración
    estado = models.CharField(
        max_length=20,
        choices=EstadoSesion.choices,
        default=EstadoSesion.PROGRAMADA,
    )

    def __str__(self):
        return f"Sesion {self.nombre} - {self.get_estado_display()}"