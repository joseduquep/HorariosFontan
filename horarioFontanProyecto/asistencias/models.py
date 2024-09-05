# asistencias/models.py
from django.db import models

class Asistencia(models.Model):
    horario = models.ForeignKey('horarios.Horario', on_delete=models.CASCADE)
    estudiante = models.ForeignKey('estudiantes.Estudiante', on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.BooleanField(default=False)
    notas = models.CharField(max_length=255, blank=True, null=True)

class Auditoria(models.Model):
    accion = models.CharField(max_length=255)
    estudiante = models.ForeignKey('estudiantes.Estudiante', on_delete=models.CASCADE)
    datos_anteriores = models.TextField(blank=True, null=True)
    datos_nuevos = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(blank=True, null=True)
