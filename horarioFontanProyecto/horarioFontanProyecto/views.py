from django.http.response import HttpResponse
from django.shortcuts import render


def vista_principal(request):
    return HttpResponse("ESTA ES LA VISTA PRINCIPAL")