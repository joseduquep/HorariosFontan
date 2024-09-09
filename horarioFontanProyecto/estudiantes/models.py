# estudiantes/models.py
from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cedula = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    nivel_autonomia = models.CharField(max_length=50)
    vacaciones_prolongadas = models.BooleanField(default=False)
    grado = models.CharField(max_length=50)
    taller = models.ForeignKey('horarios.Taller', on_delete=models.SET_NULL, null=True, blank=True)
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    tutor = models.ForeignKey('usuarios.Tutor', on_delete=models.SET_NULL, null=True, blank=True)
    tutor = models.ForeignKey('usuarios.Tutor', on_delete=models.SET_NULL, null=True, blank=True)
    foto = models.ImageField(upload_to='estudiantes/images', default='estudiantes/images/DSC_137999.jpg', blank=True, null=True)
    foto2 = models.ImageField(upload_to='estudiantes/images', default='estudiantes/images/DSC_137999.jpg', blank=True, null=True)


class EstudianteTaller(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
    taller = models.ForeignKey('horarios.Taller', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('estudiante', 'taller')
