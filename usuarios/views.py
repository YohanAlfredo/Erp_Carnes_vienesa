## manejar las peticiones de los usuarios
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Formulario_acceso
from .models import Rol, Usuario_Rol

def vista_inicio_seccion(request): #Login_view
    if request.usuario.is_authenticated:
        return redirect('dashboard')  # Redirige al panel principal si el usuario ya ha iniciado sesión
    
    if request.method == 'POST':
    
        formulario = Formulario_acceso(request.POST)
        if formulario.is_valid():
            usuario_nombre = formulario.cleaned_data.get('usuario_nombre')
            contraseña = formulario.cleaned_data.get('contraseña')
            usuario = authenticate(usuario_nombre=usuario_nombre, contraseña=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('dashboard')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
                
    else:
        formulario = Formulario_acceso()
    
    return render(request, 'usuarios/acceso.html', {'formulario': formulario})

@login_required
def vista_cerrar_sesion(request): #
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('acceso')
        
            