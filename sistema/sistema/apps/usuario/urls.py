from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from apps.usuario.views import *

urlpatterns = [
    path('inicio_usuarios/', InicioUsuarios.as_view(), name='inicio_usuarios'),
    path('listado_usuarios/', ListadoUsuario.as_view(),name='listar_usuarios'),
    path('registrar_usuario/',RegistrarUsuario.as_view(),name = 'registrar_usuario'),
    path('actualizar_usuario/<int:pk>/',EditarUsuario.as_view(), name = 'actualizar_usuario'),
    path('eliminar_usuario/<int:pk>/',EliminarUsuario.as_view(), name='eliminar_usuario'),

    # URLS GENERALES

    path('listado-usuario-alumnos/',ListadoUsuarioAlumno.as_view(), name = 'listado_usuario_alumnos'),
    path('detalle-usuario-alumno/<int:pk>/',DetalleUsuarioAlumno.as_view(), name = 'detalle_usuario_alumno'),
    path('listado-usuario-profesor/',ListadoUsuarioProfesor.as_view(), name = 'listado_usuario_profesor'),
    path('detalle-usuario-profesor/<int:pk>/',DetalleUsuarioProfesor.as_view(), name = 'detalle_usuario_profesor'),
    path('calendario/',Calendario.as_view(), name = 'calendario'),
]