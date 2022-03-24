from apps.institucion.models import Alumno
import json
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView,DetailView
from apps.usuario.models import Rol, Usuario
from .forms import FormularioLogin,FormularioUsuario
from apps.usuario.mixins import LoginYSuperStaffMixin,ValidarPermisosMixin,LoginMixin
from apps.institucion.models import Fecha

#class Inicio(LoginYSuperStaffMixin,TemplateView): antes no me dejaba iniciar desde el login y tenia que ir al admin para iniciar el usuario
class Inicio(LoginRequiredMixin,TemplateView):
    #clase que renderiza el index del sistema
    template_name = 'index.html'
    groups_required = ['alumno','administrador','profesor']

    def get(self,request,*args,**kwargs):
        contador = 0
        grupos_usuario = request.user.groups.all().values('name')
        for grupo in grupos_usuario:
            if grupo['name'] in self.groups_required:
                contador += 1
        if contador == len(self.groups_required):
            return render(request,self.template_name)
        else:
            print("NO ESTA DENTRO DE LOS GRUPOS")
        # agregar un permiso
        # usuario.user_permissions.add(permiso1,permiso2,...)
        # usuario.user_permissions.remove(permiso1,permiso2,...)
        # usuario.user_permissions.set([lista_permisos])
        # usuario.user_permissions.clear()
        
        return render(request,self.template_name)


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class InicioUsuarios(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name='usuarios/listar_usuario.html'
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')

class ListadoUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, ListView):
    model = Usuario
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('usuarios:inicio_usuarios')

class RegistrarUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files= request.FILES )
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('usuarios:inicio_usuarios')

class EditarUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/editar_usuario.html'
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('usuarios:inicio_usuarios')

class EliminarUsuario(LoginYSuperStaffMixin, ValidarPermisosMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar_usuario.html'
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            usuario = self.get_object()
            usuario.is_active = False
            usuario.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('usuarios:inicio_usuarios')

class ListadoUsuarioAlumno(LoginMixin,ListView):
    model = Usuario
    paginate_by = 12
    second_model=Alumno
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')

    #paginate_by = 6
    template_name = 'usuarios/usuarios_alumno.html'
    
    def get_queryset(self):        
        queryset = self.model.objects.filter(is_active = True,tipo__icontains = 'Alumno')
        return queryset 

class DetalleUsuarioAlumno(LoginMixin,DetailView):
    model = Usuario
    template_name = 'usuarios/detalle_usuario_alumno.html'
    #falta poner al boton que pueda enviar un mensaje desde el correo del profesor 
    """def get(self,request,*agrs,**kwargs):
        if self.get_object().tipo__icontains = 'Alumno':
            return render(request,self.template_name,{'object':self.get_object()})
        return redirect('usuario:detalle_usuario_alumno')"""

class ListadoUsuarioProfesor(LoginMixin,ListView):
    model = Usuario
    paginate_by = 6
    permission_required = ('usuario.view_usuario', 'usuario.add_usuario',
                           'usuario.delete_usuario', 'usuario.change_usuario')

    #paginate_by = 6
    template_name = 'usuarios/usuarios_profesor.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(is_active = True,tipo__icontains = 'Profesor')
        return queryset 

class DetalleUsuarioProfesor(LoginMixin,DetailView):
    model = Usuario
    template_name = 'usuarios/detalle_usuario_profesor.html'

class Calendario(LoginMixin,ListView):
    model = Fecha
    template_name = 'usuarios/calendario.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(estado = True)
        return queryset

