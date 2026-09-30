from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario_Rol
# Dashboard o panel de control principal de la aplicación
# Calcular los permisos que tiene el usuario (0,1,2)  

@login_required
def vista_dashboard(request):
    
    usuario_roles = Usuario_Rol.objects.filter(usuario_id=request.user)
    
    permisos = {
        "administrador": 0,
        "recepcion_materias_primas": 0,
        "planta_produccion": 0,
        "control_calidad": 0,
        "tajado": 0,
        "bodega": 0
    }
    
    for usuario_rol in usuario_roles:
        rol = usuario_rol.rol
        for module in permisos.keys():
            permisos_actuales = getattr(rol, module) #current_permissions 
            if permisos_actuales > permisos[module]:
                permisos[module] = permisos_actuales
    
    context = {
        "usuario": request.usuario,
        "permisos": permisos,
        "roles": [ur.rol.rol_nombre for ur in usuario_roles],
    }
    
    """El contexto de un template (o motor de plantillas) en programación es el conjunto de datos, 
    variables y funciones que se le entregan a una plantilla para que los procese y dibuje el resultado final en pantalla"""
    
    return render(request, "core/dashboard.html", context)