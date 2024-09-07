from django.urls import path
from . import views


app_name = 'estudiantes'
# estudiantes/..

urlpatterns = [
    path('perfil/<int:num_alumno>', views.num_alumno_vista, name='vista_num_alumno'),
    path('perfil/', views.vista_perfil, name='pagina-estudiantes'),
    path('', views.vista_home, name='vista_estudiantes'),
    path('registro_estudiante/', views.registro_estudiante, name='registro_estudiante'),
    #path('estudiantes_por_taller/<str:taller_id>/', views.estudiantes_por_taller, name='estudiantes_por_taller'),
]
