from django.urls import path
from . import views


# usuarios/..
app_name= 'usuarios'

urlpatterns = [
    path('', views.inicio, name='vista_inicio'),
    path('registro/', views.registro_usuario, name='vista_registro_usuario'),
]