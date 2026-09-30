## DEFINICIÓN DE MODELOS PARA LA APLICACIÓN DE USUARIOS
## los modelos definien como se estructura la base de datos 

from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    usuario_id = models.AutoField(primary_key=True)
    usuario_nombre = models.CharField(max_length=150, unique=True)
    contraseña = models.CharField(max_length=128)
    
    Usuario_Nombre_Campo = usuario_nombre
    
    class Meta:
        tabla_bases_de_datos = 'usuarios'
        nombre_detallado = 'Usuario'
        nombre_detallado_plural = 'Usuarios'
        
class Rol(models.Model):
    OPCIONES_PERMISOS = [ # permission_options
        (0, "No acceso"),
        (1, "Acceso de solo lectura"),
        (2, "Acceso de lectura y modificar"),
    ]
    
    rol_nombre = models.CharField(max_length=50, primary_key=True)  
    administrador = models.IntegerField(choices=OPCIONES_PERMISOS, default=0)
    recepcion_materias_primas = models.IntegerField(choices=OPCIONES_PERMISOS, default=0)
    planta_produccion = models.IntegerField(choices=OPCIONES_PERMISOS, default=0)
    control_calidad = models.IntegerField(choices=OPCIONES_PERMISOS, default=0)
    tajado = models.IntegerField(choices=OPCIONES_PERMISOS, default=0)
    bodega = models.IntegerField(choices=OPCIONES_PERMISOS, default=0)
    
    class Meta:
        tabla_bases_de_datos = 'roles'
        nombre_detallado = 'Rol'
        nombre_detallado_plural = 'Roles'
            
    def __str__(self):
         return self.rol_nombre
     
class Usuario_Rol(models.Model):

    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    class Meta:
        tabla_bases_de_datos = 'usuario_rol'   
        nombre_detallado = 'Usuario Rol'
        nombre_detallado_plural = 'Usuarios Roles'
        Unico_rol_usuario = ("usuario_id", "rol")
        
    def __str__(self):
        return f"{self.usuario_id.usuario_nombre} - {self.rol.rol_nombre}"