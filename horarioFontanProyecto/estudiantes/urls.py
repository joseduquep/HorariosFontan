from django.urls import path
from . import views

# estudiantes/..

urlpatterns = [
    path('perfil/', views.vista_perfil, name='pagina-estudiantes'),
    path('', views.vista_estudiantes, name='estudiantes')
]
