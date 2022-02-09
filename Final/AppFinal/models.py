from pickle import TRUE
from django.db import models

# Create your models here.

class Personal(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    legajo = models.IntegerField(unique=TRUE)

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=30)
    esp_activa = models.BooleanField()

class EquipoTrabajo(models.Model):
    equipo = models.CharField(max_length=30)
    responsable = models.CharField(max_length=30)