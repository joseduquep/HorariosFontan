# asistencias/models.py
from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Asistencia(models.Model):
    # Definimos las opciones para el campo 'estado'
    ESTADO_CHOICES = [
        ('P', 'Presente'),
        ('A', 'Ausente')
    ]
    
    horario = models.ForeignKey('horarios.Horario', on_delete=models.CASCADE, null=True, blank=True)
    estudiante = models.ForeignKey('estudiantes.Estudiante', on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField()
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES,  # Aplicamos las opciones
        default='P'  # Valor por defecto, en este caso 'Presente'
    )
    notas = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Asistencia de {self.estudiante.nombre} en {self.fecha}: {self.get_estado_display()}"


class Auditoria(models.Model):
    accion = models.CharField(max_length=255)
    estudiante = models.ForeignKey('estudiantes.Estudiante', on_delete=models.CASCADE, null=True, blank=True)
    datos_anteriores = models.TextField(blank=True, null=True)
    datos_nuevos = models.TextField(blank=True, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Acción: {self.accion}, Estudiante: {self.estudiante.nombre}, Usuario: {self.usuario.username}, Fecha: {self.fecha}"

