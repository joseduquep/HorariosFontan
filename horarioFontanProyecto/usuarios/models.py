# usuarios/models.py
from django.contrib.auth.models import User
from django.db import models
    
# usuarios/models.py

# class Usuario(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     rol = models.CharField(max_length=50)
#     fecha_creacion = models.DateField(auto_now_add=True)
#     ultimo_login = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f"Perfil de {self.user.username}"

class Tutor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Tutor: {self.usuario.username if self.usuario else 'Sin usuario asignado'}"


