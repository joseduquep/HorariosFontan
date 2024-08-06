from django.urls import path
from . import views

# estudiantes/..

urlpatterns = [
    path('', views.vista_estudiante, name='pagina-estudiantes')
]
