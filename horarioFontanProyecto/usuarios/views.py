from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def inicio(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'estudiantes/home.html')
        else:
            messages.error(request, "Error al iniciar sesión. Por favor, inténtalo de nuevo.")
            return render(request, 'usuarios/inicio.html')
    else:
        return render(request, 'usuarios/inicio.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "¡Te registraste correctamente!")
                return render(request, 'estudiantes/home.html')
    else:
        form = SignUpForm()

    return render(request, 'usuarios/registro.html', {'form': form})


def logout_user(request):
	logout(request)
	messages.success(request, "Cerraste sesion correctamente...")
	return render(request, 'usuarios/inicio.html')