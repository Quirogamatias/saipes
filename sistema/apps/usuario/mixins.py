from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy

class LoginYSuperStaffMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')

class LoginMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')

class ValidarPermisosMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required,str): return (self.permission_required)
        else: return self.permission_required

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect(self.get_url_redirect())

class ValidarAlumno(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.tipo == "Alumno" or request.user.is_superuser or request.user.tipo == "Administrador":
                return super().dispatch(request, *args, **kwargs)
            else:
                messages.error(request, 'No tienes permisos para realizar esta acción.') 
        return redirect('index')

class ValidarProfesor(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.tipo == "Profesor" or request.user.is_superuser or request.user.tipo == "Administrador":
                return super().dispatch(request, *args, **kwargs)
            else:
                messages.error(request, 'No tienes permisos para realizar esta acción.') 
        return redirect('index')

class ValidarAdministrador(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.tipo == "Administrador":
                return super().dispatch(request, *args, **kwargs)
            else:
                messages.error(request, 'No tienes permisos para realizar esta acción.') 
        return redirect('index')
#si funciona el validaralumno, solo que cuando mustro los datos de un alumno
#  solo tendira que mostrar el de ese solo alumno y no el de todos, para eso tengo que crear otro template que haga eso u otro vista qcon esa definicion
