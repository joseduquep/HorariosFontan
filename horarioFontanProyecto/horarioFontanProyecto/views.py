from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def vista_principal(request):
    logout(request)
    return render(request, 'index.html')