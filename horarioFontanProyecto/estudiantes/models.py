from django.db import models

# Create your models here.

# este es un modelo de prueba para testear la conexion con MySQL
class TestModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"El nombre asignado a este objeto es {self.name}"