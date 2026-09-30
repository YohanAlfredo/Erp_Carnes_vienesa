from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Rol, Usuario_Rol

#vista de administración para el modelo Usuario
"""este codigo define los poderes de administración para crear, editar y eliminar usuarios en la aplicación, además de definir los roles para cada usuario y sus permisos"""

@admin.register(Usuario)
class CustomUsuarioAdmin(UserAdmin):
    list_display = ('usuario_nombre', 'email', 'primer_nombre','apellido' 'is_staff', 'is_active') #EL administrador tendra estos campos
    list_filter = ('is_staff', 'is_active', 'date_joined') #se puede filtrar por estos campos
    search_fields = ('usuario_nombre', 'email', 'primer_nombre', 'apellido') #se puede buscar por estos campos
    
@admin.register(Rol)#para poder manejar los roles
class RolAdmin(admin.ModelAdmin):
    list_display = ('rol_nombre', 'administrador', 'recepcion_materias_primas', 'planta_produccion', 'control_calidad', 'tajado', 'bodega')
    list_filter = ('administrador', 'recepcion_materias_primas', 'planta_produccion', 'control_calidad', 'tajado', 'bodega')
    search_fields = ('rol_nombre',)
    
@admin.register(Usuario_Rol) #para poder manejar los roles de los usuarios
class Usuario_RolAdmin(admin.ModelAdmin):
    list_display = ('usuario_id', 'rol')
    list_filter = ('rol')
    search_fields = ('usuario_id__usuario_nombre', 'rol__rol_nombre')
    
