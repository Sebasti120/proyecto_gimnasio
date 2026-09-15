from django.db import models

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100, default='')
    ubicacion = models.CharField(max_length=150, default='')
    categoria = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True, default='')
    estado_equipo = models.CharField(max_length=50)



    def __str__(self):
        return f"{self.marca} - {self.categoria} ({self.numero_serie})"
    

class Mantenimiento(models.Model):
    equipo = models.TextField()
    descripcion_problema = models.TextField()
    fecha_mantenimiento = models.DateField()                   
    fecha_reporte = models.DateField(auto_now_add=True)          
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"Mantenimiento de {self.equipo} - {self.estado}"