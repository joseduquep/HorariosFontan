from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.


def inicio(request):
	# Check to see if logging in
	if request.method == 'POST':
		email = request.POST['correo']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('vista_estudiantes')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('vista_inicio')
	else:
		return render(request, 'usuarios/inicio.html')


def registro_usuario(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, "Te registraste correctamente! Bienvenido!")
            return redirect('vista_inicio')
    else:
        form = SignUpForm()

    return render(request, 'usuarios/registro.html', {'form': form})