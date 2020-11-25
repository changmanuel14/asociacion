# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Especialidad(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria


class Subespecialidad(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria

class Asociado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_renMem = models.DateField()
    telefono = models.IntegerField()
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    especialidad = models.ForeignKey(
        Especialidad, related_name="asociados", on_delete=models.CASCADE
    )
    subespecialidad = models.ForeignKey(
        Subespecialidad, related_name="asociados", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre

