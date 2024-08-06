from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista_estudiante(request):
    # estudiantes/templates/estudiantes/perfil.html
    return render(request, 'estudiantes/perfil.html')