from django.urls import path
from . import views

# estudiantes/..

urlpatterns = [
    path('perfil/<int:num_alumno>', views.num_alumno_vista, name='vista_num_alumno'),
    path('perfil/', views.vista_perfil, name='pagina-estudiantes'),
    path('', views.vista_home, name='vista_estudiantes'),
]
