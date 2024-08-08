from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista_perfil(request):
    # estudiantes/templates/estudiantes/perfil.html
    return render(request, 'estudiantes/perfil.html')


def vista_estudiantes(request):
    # estudiantes/templates/estudiantes/home.hmtl
    return render(request, 'estudiantes/home.html')