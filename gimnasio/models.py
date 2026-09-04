from django.core.exceptions import ValidationError
from django.db import models


class Rutina(models.Model):
    id_rutina = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=50)
    nombre_rutina = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_rutina


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
        if errores:
            raise ValidationError(errores)

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
        if errores:
            raise ValidationError(errores)

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