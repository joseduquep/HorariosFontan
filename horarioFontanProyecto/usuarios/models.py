# usuarios/models.py
from django.contrib.auth.models import User
from django.db import models
    
# usuarios/models.py

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)
    ultimo_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

class Tutor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, default=1)
    # No activar:
    #taller = models.ForeignKey('horarios.Taller', on_delete=models.SET_NULL, null=True, blank=True)

