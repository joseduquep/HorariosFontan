# usuarios/models.py
from django.contrib.auth.models import User
from django.db import models

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
