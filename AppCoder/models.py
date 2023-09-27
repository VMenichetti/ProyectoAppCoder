from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    fecha_creacion=models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.camada}'

    class Meta():
        verbose_name='Course'
        verbose_name_plural='The Courses'
        ordering=('nombre','-camada')
        unique_together=('nombre','camada')

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=256, null=True)