from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Tutor


def inicio(request):
    logout(request)
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
    logout(request)
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)  
        if form.is_valid():
            user = form.save(commit=False)  # No guardar aún
            user.set_password(form.cleaned_data['password1'])
            user.save()  # Ahora guardar el usuario
            user_type = form.cleaned_data['user_type']
            
            if user_type == 'tutor':
                Tutor.objects.create(
                    usuario=user,
                    foto=form.cleaned_data.get('foto')
                )
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return render(request, 'estudiantes/home.html')
    else:
        form = SignUpForm()

    return render(request, 'usuarios/registro.html', {'form': form})




def logout_user(request):
	logout(request)
	messages.success(request, "Cerraste sesion correctamente...")
	return render(request, 'usuarios/inicio.html')


def perfil_usuario(request):
    tutor = Tutor.objects.get(usuario=request.user)
    return render(request, 'usuarios/perfil_usuario.html/', {'tutor': tutor})

def perfil_modificar(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('nombre')
        user.last_name = request.POST.get('apellido')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')

        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password and password == password2:
            user.set_password(password)
        
        user.save()
        messages.success(request, '¡Perfil actualizado exitosamente!')
        return render(request, 'usuarios/perfil_usuario.html')

    return render(request, 'usuarios/perfil_modificar.html')