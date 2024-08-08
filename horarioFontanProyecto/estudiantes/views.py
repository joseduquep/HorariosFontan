from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def vista_perfil(request):
    # estudiantes/templates/estudiantes/perfil.html
    return render(request, 'estudiantes/perfil.html')


def vista_home(request):
    # estudiantes/templates/estudiantes/home.hmtl
    return render(request, 'estudiantes/home.html')


alumnos = {
    "repre1": 'Nico',
    "repre2": "Pedro",
    "repre3": "Jose"
}

def num_alumno_vista(request, num_alumno):
    alumno_lista = list(alumnos.values()) # ['Nico', 'Pedro', ...]
    alumno = alumno_lista[num_alumno]
    return HttpResponseRedirect(alumno)