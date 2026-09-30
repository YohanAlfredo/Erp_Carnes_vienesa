from django.urls import path
from . import views
#creación de las rutas de acceso a las vistas de los usuarios

urlpatterns = [ #define las rutas de acceso a las vistas de la aplicación de usuarios
    path('acceso/', views.vista_inicio_seccion, name='acceso'),
    path('cerrar_sesion/', views.vista_cerrar_sesion, name='cerrar_sesion'),
]