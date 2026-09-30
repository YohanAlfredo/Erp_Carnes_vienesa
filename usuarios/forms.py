## formulario del ACCESO personalizado
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

class Formulario_acceso(AuthenticationForm): #LoginForm)
    
    usuario_nombre = forms.CharField(
        label ='Nombre de usuario', #etiqueta
        widget = forms.TextInput(attrs={ 
            "class": "form-control", # "clase": "control_formulario"
            "placeholder": "Ingrese su nombre de usuario", #"Marcador_posición": "Ingrese su nombre de usuario",
        })
    )
    
    contraseña = forms.CharField(
        label ='Contraseña', #etiqueta 
        widget = forms.PasswordInput(attrs={
            "class": "form-control", # "clase": "control_formulario"
            "placeholder": "Ingrese su contraseña", #"Marcador_posición": "Ingrese su contraseña",
        })
    )
    
    class Meta:
        
        model = Usuario # modelo = Usuario
        fields = ['usuario_nombre', 'contraseña'] # campos = ['usuario_nombre', 'contraseña']