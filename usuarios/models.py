## DEFINICIÓN DE MODELOS PARA LA APLICACIÓN DE USUARIOS
## los modelos definien como se estructura la base de datos 

from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    usuario_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    
    USERNAME_FIELD = 'username'   #le decimos a django que campo usar para login

    
    class Meta:
        db_table = 'usuarios'       # tabla_bases_de_datos
        verbose_name = 'Usuario'            # nombre_detallado
        verbose_name_plural = 'Usuarios'    # nombre_detallado_plural
        
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
        db_table = 'roles'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
            
    def __str__(self):
         return self.rol_nombre
     
class Usuario_Rol(models.Model):

    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'usuario_rol'
        verbose_name = 'Usuario Rol'
        verbose_name_plural = 'Usuarios Roles'
        unique_together = ("usuario_id", "rol")     #Unico_rol_usuario
        
    def __str__(self):
        return f"{self.usuario_id.username} - {self.rol.rol_nombre}"
    