# horarios/models.py
from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Taller(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    cupo_maximo = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    cupo_actual = models.IntegerField(default=0)
    tutor = models.ForeignKey('usuarios.Tutor', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} (Cupo: {self.cupo_actual}/{self.cupo_maximo})"



class Bloque(models.Model):
    nombre = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    tipo = models.CharField(max_length=50)  # Ejemplo: 'clase', 'descanso', etc.

class Horario(models.Model):
    estudiante = models.ForeignKey('estudiantes.Estudiante', on_delete=models.CASCADE, null=True, blank=True)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE, null=True, blank=True)
    tutor = models.ForeignKey('usuarios.Tutor', on_delete=models.CASCADE, null=True)
    bloque = models.ForeignKey(Bloque, on_delete=models.CASCADE, null=True, blank=True)
