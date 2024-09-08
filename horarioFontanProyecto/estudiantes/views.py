from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Estudiante
from .forms import EstudianteForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.
def vista_perfil(request):
    # estudiantes/templates/estudiantes/perfil.html
    return render(request, 'estudiantes/perfil.html')


def vista_home(request):
    # estudiantes/templates/estudiantes/home.hmtl
    query = not query
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/home.html', {'estudiante':estudiantes})


def search(request):
    query = request.GET.get('query')
    estudiantes = Estudiante.objects.filter(nombre__icontains=query)
    return render(request, 'estudiantes/home.html', {'estudiantes': estudiantes, 'query': query})

alumnos = {
    "repre1": 'Nico',
    "repre2": "Pedro",
    "repre3": "Jose"
}

def num_alumno_vista(request, num_alumno):
    alumno_lista = list(alumnos.values()) # ['Nico', 'Pedro', ...]
    alumno = alumno_lista[num_alumno]
    return HttpResponseRedirect(alumno)

def registro_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            Estudiante = form.save()
            Estudiante.nombre = form.cleaned_data['nombre']
            Estudiante.apellido = form.cleaned_data['apellido']
            Estudiante.cedula = form.cleaned_data['cedula']
            Estudiante.nivel_autonomia = form.cleaned_data['nivel_autonomia']
            Estudiante.taller = form.cleaned_data['taller']
            Estudiante.grado = form.cleaned_data['grado']
            Estudiante.foto= form.cleaned_data['foto']
            if Estudiante is not None:
                return render(request, 'estudiantes/home.html')
    else:
        form = EstudianteForm()

    return render(request, 'estudiantes/registro_estudiante.html', {'form': form})

#CUANDO YA ESTEN CREADO EL MODELO DE TALLER Y DE ESTUDIANTES, PARA QUE CADA TALLER REDIRIJA HACIA EL ADECUADO
#def estudiantes_por_taller(request, taller_id):
#    taller = Taller.objects.get(nombre=taller_id)
#   estudiantes = Estudiante.objects.filter(taller=taller)
#  return render(request, 'home.html', {'taller': taller, 'Estudiante': estudiantes})
