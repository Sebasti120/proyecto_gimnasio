from django.db import models

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100, default='')
    ubicacion = models.CharField(max_length=150, default='')
    id_gimnasio = models.ForeignKey('gimnasioapp.Gimnasio', on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True, default='')
    estado_equipo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.categoria} ({self.estado_equipo})"

    def __str__(self):
        return f"{self.marca} - {self.categoria} ({self.numero_serie})"
    

class Mantenimiento(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='mantenimientos')
    fecha_mantenimiento = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=50, default='pendiente')

    def __str__(self):
        return f"Mantenimiento {self.equipo.categoria} - {self.fecha_mantenimiento}"