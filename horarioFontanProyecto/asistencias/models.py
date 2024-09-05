# asistencias/models.py
from django.db import models

class Asistencia(models.Model):
    horario = models.ForeignKey('horarios.Horario', on_delete=models.CASCADE, null=True, blank=True)
    estudiante = models.ForeignKey('estudiantes.Estudiante', on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField()
    estado = models.BooleanField(default=False)
    notas = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"notas de la asistencia: {self.notas}"

class Auditoria(models.Model):
    accion = models.CharField(max_length=255)
    estudiante = models.ForeignKey('estudiantes.Estudiante', on_delete=models.CASCADE, null=True, blank=True)
    datos_anteriores = models.TextField(blank=True, null=True)
    datos_nuevos = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, default=1)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Accion: {self.accion}"
