import json
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse, request
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView,DetailView
from apps.usuario.mixins import LoginYSuperStaffMixin,ValidarPermisosMixin,LoginMixin
from apps.usuario.models import Usuario
from .models import *
from .forms import *


class Inicio(TemplateView):
    template_name = 'index.html'

class InicioAdministrador(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/administrador/listar_administrador.html'
    permission_required = ('institucion.view_administrador', 'institucion.add_administrador',
                           'institucion.delete_administrador', 'institucion.change_administrador')

class InicioPromedioAsistencia(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/porcentaje/listar_porcentaje.html'
    permission_required = ('institucion.view_promedioasistencia', 'institucion.add_promedioasistencia',
                           'institucion.delete_promedioasistencia', 'institucion.change_promedioasistencia')


class InicioCurso(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/curso/listar_curso.html'
    permission_required = ('institucion.view_curso', 'institucion.add_curso',
                           'institucion.delete_curso', 'institucion.change_curso')

class InicioAlumno(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/alumno/listar_alumno.html'
    permission_required = ('institucion.view_alumno', 'institucion.add_alumno',
                           'institucion.delete_alumno', 'institucion.change_alumno')

class InicioCarrera(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/carrera/listar_carrera.html'
    permission_required = ('institucion.view_carrera', 'institucion.add_carrera',
                           'institucion.delete_carrera', 'institucion.change_carrera')


class InicioHorario(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/horario/listar_horario.html'
    permission_required = ('institucion.view_horario', 'institucion.add_horario',
                           'institucion.delete_horario', 'institucion.change_horario')

class InicioInscripcion(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/inscripcion/listar_inscripcion.html'
    permission_required = ('institucion.view_inscripcion', 'institucion.add_inscripcion',
                           'institucion.delete_inscripcion', 'institucion.change_inscripcion')

class InicioMateria(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/materia/listar_materia.html'
    permission_required = ('institucion.view_materia', 'institucion.add_materia',
                           'institucion.delete_materia', 'institucion.change_materia')

class InicioNotas(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/notas/listar_notas.html'
    permission_required = ('institucion.view_notas', 'institucion.add_notas',
                           'institucion.delete_notas', 'institucion.change_notas')

class InicioProfesor(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/profesor/listar_profesor.html'
    permission_required = ('institucion.view_profesor', 'institucion.add_profesor',
                           'institucion.delete_profesor', 'institucion.change_profesor')

class InicioAsistencia(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/asistencia/listar_asistencia.html'
    permission_required = ('institucion.view_asistencia', 'institucion.add_asistencia',
                           'institucion.delete_asistencia', 'institucion.change_asistencia')

class InicioFecha(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/fecha/listar_fecha.html'
    permission_required = ('institucion.view_fecha', 'institucion.add_fecha',
                           'institucion.delete_fecha', 'institucion.change_fecha')

class CrearCurso(LoginYSuperStaffMixin,ValidarPermisosMixin,CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'institucion/curso/crear_curso.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_curso = Curso(
                    nombre = form.cleaned_data.get('nombre'),
                    capacidad = form.cleaned_data.get('capacidad'),
                    turno = form.cleaned_data.get('turno')
                )
                nuevo_curso.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_curso')

class ListadoCursos(LoginYSuperStaffMixin,ValidarPermisosMixin,ListView):
    model = Curso   
    permission_required = ('institucion.view_curso', 'institucion.add_curso',
                           'institucion.delete_curso', 'institucion.change_curso')

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_curso')

class ActualizarCurso(LoginYSuperStaffMixin,ValidarPermisosMixin,UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'institucion/curso/curso.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_curso')

class EliminarCurso(LoginYSuperStaffMixin,ValidarPermisosMixin,DeleteView):
    model = Curso
    template_name = 'institucion/curso/eliminar_curso.html'

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            curso = self.get_object()
            curso.estado = False
            curso.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('institucion:inicio_curso')

class ListadoHorarios(LoginYSuperStaffMixin, ValidarPermisosMixin,View):
    model = Horario
    permission_required = ('institucion.view_horario', 'institucion.add_horario',
                           'institucion.delete_horario', 'institucion.change_horario')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['horarios'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_horario')

class ActualizarHorario(LoginYSuperStaffMixin, ValidarPermisosMixin,UpdateView):
    model = Horario
    form_class = HorarioForm
    template_name = 'institucion/horario/horario.html'
    permission_required = ('institucion.view_horario', 'institucion.add_horario',
                           'institucion.delete_horario', 'institucion.change_horario')
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_horario')

class CrearHorario(LoginYSuperStaffMixin, ValidarPermisosMixin,CreateView):
    model = Horario
    form_class = HorarioForm
    template_name = 'institucion/horario/crear_horario.html'
    permission_required = ('institucion.view_horario', 'institucion.add_horario',
                           'institucion.delete_horario', 'institucion.change_horario')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
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
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'institucion: inicio_horario' )

class EliminarHorario(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):
    model = Horario
    template_name = 'institucion/horario/eliminar_horario.html'
    permission_required  = ( 'institucion.view_horario' , 'institucion.add_horario' ,
                           'institucion.delete_horario' , 'institucion.change_horario' )

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            horario = self.get_object()
            horario.estado = False
            horario.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('institucion:inicio_horario')

class ListadoAlumnos(LoginYSuperStaffMixin, ValidarPermisosMixin,View):
    model = Alumno
    permission_required = ('institucion.view_alumno', 'institucion.add_alumno',
                           'institucion.delete_alumno', 'institucion.change_alumno')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['alumnos'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_alumno')

class ActualizarAlumno(LoginYSuperStaffMixin, ValidarPermisosMixin,UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'institucion/alumno/alumno.html'
    permission_required = ('institucion.view_alumno', 'institucion.add_alumno',
                           'institucion.delete_alumno', 'institucion.change_alumno')
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_alumno')

class CrearAlumno(LoginYSuperStaffMixin, ValidarPermisosMixin,CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'institucion/alumno/crear_alumno.html'
    permission_required = ('institucion.view_alumno', 'institucion.add_alumno',
                           'institucion.delete_alumno', 'institucion.change_alumno')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
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
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        return  redirect ( 'institucion: inicio_alumno' )

class EliminarAlumno(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):
    model = Alumno
    template_name = 'institucion/alumno/eliminar_alumno.html'
    permission_required  = ( 'institucion.view_alumno' , 'institucion.add_alumno' ,
                           'institucion.delete_alumno' , 'institucion.change_alumno' )

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            alumno = self.get_object()
            alumno.estado = False
            alumno.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('institucion:inicio_alumno')

class ListadoInscripciones(LoginYSuperStaffMixin, ValidarPermisosMixin,View):
    model = Inscripcion
    permission_required = ('institucion.view_inscripcion', 'institucion.add_inscripcion',
                           'institucion.delete_inscripcion', 'institucion.change_inscripcion')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['inscripciones'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_inscripcion')

class ActualizarInscripcion(LoginYSuperStaffMixin,ValidarPermisosMixin,UpdateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = 'institucion/inscripcion/inscripcion.html'
    permission_required = ('institucion.view_inscripcion', 'institucion.add_inscripcion',
                           'institucion.delete_inscripcion', 'institucion.change_inscripcion')
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_inscripcion')

class CrearInscripcion(LoginYSuperStaffMixin, ValidarPermisosMixin,CreateView):
    model = Inscripcion
    form_class = InscripcionForm
    second_form_class = PromedioAsistenciaForm
    template_name = 'institucion/inscripcion/crear_inscripcion.html'
    permission_required = ('institucion.view_inscripcion', 'institucion.add_inscripcion',
                           'institucion.delete_inscripcion', 'institucion.change_inscripcion')

    def get_context_data(self, **kwargs):
        context = super(CrearInscripcion, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            form2 = self.second_form_class(data = request.POST,files = request.FILES)
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'institucion: inicio_inscripcion' )

class EliminarInscripcion(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):
    model = Inscripcion
    template_name = 'institucion/inscripcion/eliminar_inscripcion.html'
    permission_required  = ( 'institucion.view_inscripcion' , 'institucion.add_inscripcion' ,
                           'institucion.delete_inscripcion' , 'institucion.change_inscripcion' )

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            inscripcion = self.get_object()
            inscripcion.estado = False
            inscripcion.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('institucion:inicio_inscripcion')

class ListadoAdministradores(LoginYSuperStaffMixin, ValidarPermisosMixin,ListView):

    model = Administrador
    permission_required = ('institucion.view_administrador', 'institucion.add_administrador',
                           'institucion.delete_administrador', 'institucion.change_administrador')

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['administradores'] = self.get_queryset() #agregamos la consulta al contexto
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json',self.get_queryset()), 'application/json')
        else:
            return redirect('institucion:inicio_administrador')

class ActualizarAdministrador(LoginYSuperStaffMixin,ValidarPermisosMixin,UpdateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'institucion/administrador/administrador.html'
    permission_required = ('institucion.view_administrador', 'institucion.add_administrador',
                           'institucion.delete_administrador', 'institucion.change_administrador')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_administrador')

class CrearAdministrador(LoginYSuperStaffMixin,ValidarPermisosMixin,CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'institucion/administrador/crear_administrador.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_administrador = Administrador(
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido'),
                    telefono=form.cleaned_data.get('telefono'),
                    domicilio=form.cleaned_data.get('domicilio'),
                    email=form.cleaned_data.get('email')
                )
                nuevo_administrador.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_administrador')

class EliminarAdministrador(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):    
    model = Administrador
    template_name = 'institucion/administrador/eliminar_administrador.html'
    permission_required = ('institucion.view_administrador', 'institucion.add_administrador',
                        'institucion.delete_administrador', 'institucion.change_administrador')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            administrador = self.get_object()
            administrador.estado = False
            administrador.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        return redirect('institucion:inicio_administrador')

class ListadoProfesores(LoginYSuperStaffMixin, ValidarPermisosMixin,ListView):
    model = Profesor
    permission_required = ('institucion.view_profesor', 'institucion.add_profesor',
                           'institucion.delete_profesor', 'institucion.change_profesor')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['profesores'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_profesor')

class ActualizarProfesor(LoginYSuperStaffMixin, ValidarPermisosMixin,UpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'institucion/profesor/profesor.html'
    permission_required = ('institucion.view_profesor', 'institucion.add_profesor',
                           'institucion.delete_profesor', 'institucion.change_profesor')
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_profesor')

class CrearProfesor(LoginYSuperStaffMixin, ValidarPermisosMixin,CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'institucion/profesor/crear_profesor.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
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
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'institucion: inicio_profesor' )

class EliminarProfesor(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):
    model = Profesor
    template_name = 'institucion/profesor/eliminar_profesor.html'
    permission_required  = ( 'institucion.view_profesor' , 'institucion.add_profesor' ,
                           'institucion.delete_profesor' , 'institucion.change_profesor' )

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            profesor = self.get_object()
            profesor.estado = False
            profesor.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('institucion:inicio_profesor')

class ListadoMaterias(LoginYSuperStaffMixin, ValidarPermisosMixin,View):
    model = Materia
    permission_required = ('institucion.view_materia', 'institucion.add_materia',
                           'institucion.delete_materia', 'institucion.change_materia')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['materias'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_materia')

class ActualizarMateria(LoginYSuperStaffMixin, ValidarPermisosMixin,UpdateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'institucion/materia/materia.html'
    permission_required = ('institucion.view_materia', 'institucion.add_materia',
                           'institucion.delete_materia', 'institucion.change_materia')
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_materia')

class CrearMateria(LoginYSuperStaffMixin, ValidarPermisosMixin,CreateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'institucion/materia/crear_materia.html'
    permission_required = ('institucion.view_materia', 'institucion.add_materia',
                           'institucion.delete_materia', 'institucion.change_materia')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
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
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'institucion: inicio_materia' )

class EliminarMateria(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):
    model = Materia
    template_name = 'institucion/materia/eliminar_materia.html'
    permission_required  = ( 'institucion.view_materia' , 'institucion.add_materia' ,
                           'institucion.delete_materia' , 'institucion.change_materia' )

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            materia = self.get_object()
            materia.estado = False
            materia.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('institucion:inicio_materia')

class ListadoNotas(LoginYSuperStaffMixin, ValidarPermisosMixin,View):
    model = Notas
    permission_required = ('institucion.view_notas', 'institucion.add_notas',
                           'institucion.delete_notas', 'institucion.change_notas')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['notas'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_notas')

class ActualizarNotas(LoginYSuperStaffMixin, ValidarPermisosMixin,UpdateView):
    model = Notas
    form_class = NotasForm
    template_name = 'institucion/notas/notas.html'
    permission_required = ('institucion.view_notas', 'institucion.add_notas',
                           'institucion.delete_notas', 'institucion.change_notas')
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_notas')

class CrearNotas(LoginYSuperStaffMixin, ValidarPermisosMixin,CreateView):
    model = Notas
    form_class = NotasForm
    template_name = 'institucion/notas/crear_notas.html'
    permission_required = ('institucion.view_notas', 'institucion.add_notas',
                           'institucion.delete_notas', 'institucion.change_notas')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
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
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'institucion: inicio_notas' )

class EliminarNotas(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):
    model = Notas
    template_name = 'institucion/notas/eliminar_notas.html'
    permission_required  = ( 'institucion.view_notas' , 'institucion.add_notas' ,
                           'institucion.delete_notas' , 'institucion.change_notas' )

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            notas = self.get_object()
            notas.estado = False
            notas.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('institucion:inicio_notas')

class ListadoCarreras(LoginYSuperStaffMixin, ValidarPermisosMixin,View):
    model = Carrera
    permission_required = ('institucion.view_carrera', 'institucion.add_carrera',
                           'institucion.delete_carrera', 'institucion.change_carrera')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['carreras'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_carrera')

class ActualizarCarrera(LoginYSuperStaffMixin, ValidarPermisosMixin,UpdateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'institucion/carrera/carrera.html'
    permission_required = ('institucion.view_carrera', 'institucion.add_carrera',
                           'institucion.delete_carrera', 'institucion.change_carrera')
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_carrera')

class CrearCarrera(LoginYSuperStaffMixin, ValidarPermisosMixin,CreateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'institucion/carrera/crear_carrera.html'
    permission_required = ('institucion.view_carrera', 'institucion.add_carrera',
                           'institucion.delete_carrera', 'institucion.change_carrera')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
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
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return  redirect ( 'institucion: inicio_carrera' )

class EliminarCarrera(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):
    model = Carrera
    template_name = 'institucion/carrera/eliminar_carrera.html'
    permission_required  = ( 'institucion.view_carrera' , 'institucion.add_carrera' ,
                           'institucion.delete_carrera' , 'institucion.change_carrera' )

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            carrera = self.get_object()
            carrera.estado = False
            carrera.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('institucion:inicio_carrera')

class ListadoAsistencia(LoginYSuperStaffMixin, ValidarPermisosMixin,View):
    model = Asistencia
    permission_required = ('institucion.view_asistencia', 'institucion.add_asistencia',
                           'institucion.delete_asistencia', 'institucion.change_asistencia')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['asistencia'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_asistencia')

class ActualizarAsistencia(LoginYSuperStaffMixin, ValidarPermisosMixin,UpdateView):
    model = Asistencia
    form_class = AsistenciaForm
    template_name = 'institucion/asistencia/asistencia.html'
    permission_required = ('institucion.view_asistencia', 'institucion.add_asistencia',
                           'institucion.delete_asistencia', 'institucion.change_asistencia')
    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_asistencia')

class CrearAsistencia(LoginYSuperStaffMixin, ValidarPermisosMixin,CreateView):
    model = Asistencia
    form_class = AsistenciaForm
    template_name = 'institucion/asistencia/crear_asistencia.html'
    permission_required = ('institucion.view_asistencia', 'institucion.add_asistencia',
                           'institucion.delete_asistencia', 'institucion.change_asistencia')

    def post(self,request,*args,**kwargs):
        #promedio = self.second_model.objects.all()
        #promedio=self.second_model.objects.get(id_materia=id_materia, id_alumno=id_alumno)
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            #form2 = self.second_form_class(data = request.POST,files = request.FILES,instance = promedio)
            if form.is_valid():
                #if promedio.id_materia == form.id_materia and promedio.id_alumno == form.id_alumno:
                 #   promedio.dias= promedio.dias + 1 
                  #  promedio.save()                        
                form.save()                
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('institucion: inicio_asistencia')

class EliminarAsistencia(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):
    model = Asistencia
    template_name = 'institucion/asistencia/eliminar_asistencia.html'
    permission_required  = ( 'institucion.view_asistencia' , 'institucion.add_asistencia' ,
                           'institucion.delete_asistencia' , 'institucion.change_asistencia' )

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            carrera = self.get_object()
            carrera.estado = False
            carrera.save()
            mensaje = f'{self.model.__name__} eliminacion correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje':mensaje,'error':error})
            response.status_code = 201
            return response            
        else: 
            return redirect('institucion:inicio_asistencia')

class CrearFecha(LoginYSuperStaffMixin,ValidarPermisosMixin,CreateView):
    model = Fecha
    form_class = FechaForm
    template_name = 'institucion/fecha/crear_fecha.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_fecha = Fecha(
                    fecha_evento = form.cleaned_data.get('fecha_evento'),
                    evento = form.cleaned_data.get('evento')
                )
                nuevo_fecha.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_fecha')   

class ListadoFecha(LoginYSuperStaffMixin, ValidarPermisosMixin,ListView):
    model = Fecha
    permission_required = ('institucion.view_fecha', 'institucion.add_fecha',
                           'institucion.delete_fecha', 'institucion.change_fecha')

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['fechas'] = self.get_queryset() #agregamos la consulta al contexto
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json',self.get_queryset()), 'application/json')
        else:
            return redirect('institucion:inicio_fecha')

class ActualizarFecha(LoginYSuperStaffMixin,ValidarPermisosMixin,UpdateView):
    model = Fecha
    form_class = FechaForm
    template_name = 'institucion/fecha/fecha.html'
    permission_required = ('institucion.view_fecha', 'institucion.add_fecha',
                           'institucion.delete_fecha', 'institucion.change_fecha')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response
        else: 
            return redirect('institucion:inicio_fecha')

class EliminarFecha(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):    
    model = Fecha
    template_name = 'institucion/fecha/eliminar_fecha.html'
    permission_required = ('institucion.view_fecha', 'institucion.add_fecha',
                        'institucion.delete_fecha', 'institucion.change_fecha')

    def delete(self,request,pk,*args,**kwargs):
        if request.is_ajax():
            fecha = self.get_object()
            fecha.estado = False
            fecha.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        return redirect('institucion:inicio_fecha')


class DetalleCarrera(LoginMixin,DetailView):
    model = Carrera
    template_name = 'institucion/carrera/detalle_carrera.html'

    """
    def get_object(self):
        id_carrera = self.kwargs.get("id_carrera")
        return get_object_or_404(Carrera, id_carrera=id_carrera)
    """

class DetalleMateria(LoginMixin,ListView):
    model = Materia    
    second_model = Inscripcion
    third_model = Alumno
    template_name = 'institucion/materia/detalle_materia.html'
    
   
    #def get_context_data(self,**kwargs):
     #   contexto= {}
      #  contexto ['materia'] = self.get_queryset() #agregamos la consulta al contexto
       # contexto['form'] = self.form_class
        #return contexto
     #solo memuestra la cantidad de inscripciones que tengo que son 4 y no las 5 materias   
    def get_context_data(self,**kwargs):
        pk = self.kwargs.get('pk')#le doy el valor del id de la materia que seleccion
        context = super().get_context_data(**kwargs)#llamo a todos lo kwargs
        context["materia"] = self.model.objects.get(pk= pk)#guardo el valor de materia con el id seleccionado
        context["inscripciones"] = self.second_model.objects.all()#guardo todos los valor de inscripcion
        context["alumnos"] = self.third_model.objects.all()
        return context#envio el contexo(valores)
        #materia= self.model.objects.get(pk= pk)              
        #inscripcion = self.second_model.objects.all()#el valor de pk esigual al id de materia, que no es el mismo que busco
       # for inscripcion in inscripcion: 
        #    inscripcion=inscripcion
        #return {'materia': materia, 'inscripcion': inscripcion}

     

    #def new_view(request):
     #   inscripcion = Inscripcion.objects.all()
      #  return render(request, 'institucion/inscripcion/detalle_materia.html', inscripcion)
    
    
    #def get_queryset(self):
     #   return self.model.objects.filter(estado = True)  

class ListadoMateriaAlumno(LoginMixin,ListView):
    model = Inscripcion
    second_model = Materia
    third_model = Alumno
    permission_required = ('institucion.view_inscripcion', 'institucion.add_inscripcion',
                           'institucion.delete_inscripcion', 'institucion.change_inscripcion')  
    template_name = 'institucion/inscripcion/listar_materia_alumno.html'
    #queryset = Inscripcion.objects.filter(id_materia__lt = 18)   
   
    def get_queryset(self):
        return self.model.objects.filter(estado = True)
        
    def new_view(request):
        materia = Materia.objects.all()
        return render(request, 'institucion/inscripcion/listar_materia_alumno.html', {'materia':materia})
    #solo me llama el id, en teoria, seguir probando
    #def get_context_data(self, *args, **kwargs):
     #   alumno = Alumno.objects.all() 
      #  materia = Materia.objects.all()
       # return {'alumno': alumno, 'materia': materia}
 
class DetalleInscripcion(LoginMixin,ListView):#si es listview me muestra todos los datos en un objeto,si es un detailview me muetraun solo dato del pk
    model = Inscripcion
    second_model = Materia
    permission_required = ('institucion.view_inscripcion', 'institucion.add_inscripcion',
                           'institucion.delete_inscripcion', 'institucion.change_inscripcion')  
    template_name = 'institucion/inscripcion/detalle_inscripcion.html'

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self):
        pk = self.kwargs.get('pk')
        inscripcion = self.model.objects.get(pk= pk)
        materia= self.second_model.objects.get(materia= inscripcion.id_materia)#el valor de pk esigual al id de materia, que no es el mismo que busco
        return {'inscripcion': inscripcion,'materia': materia}


#hacer un for o un if en la vista ya que tengo el id de materia y con eso puedo hacer las condiciones y mostrar solo lo que quiero
#tambien podria guardar los datos que necesito y despues retornar solo esos datos y mostrarlos en el template

class DetalleAlumno(LoginMixin,DetailView):
    model = Alumno
    template_name = 'institucion/alumno/detalle_alumno.html'

class AsistenciaMateria(LoginMixin,ListView):
    model = Materia    
    second_model = Asistencia
    third_model = Alumno
    template_name = 'institucion/materia/asistencia_materia.html'
    
    def get_context_data(self,**kwargs):
        pk = self.kwargs.get('pk')#le doy el valor del id de la materia que seleccion
        context = super().get_context_data(**kwargs)#llamo a todos lo kwargs
        context["materia"] = self.model.objects.get(pk= pk)#guardo el valor de materia con el id seleccionado
        context["asistencias"] = self.second_model.objects.all()#guardo todos los valor de inscripcion
        context["alumnos"] = self.third_model.objects.all()
        return context 

    #def promedio(self,**kwargs):
     #   pk = self.kwargs.get('pk')
      #  context = super().get_context_data(**kwargs)

       # cont=0
        #m=self.model.objects.get(pk= pk)
        #asi = self.second_model.objects.all()
        #al = self.third_model.objects.all()
        #for asis in asi:
         #   if asis.materia == m.id_materia:
          #      for alu in al:
           #         if alu.alumno == asi.id_alumno:
            #            cont=cont+1
             #           p=asi.asistencia
              #  return {'materia': m,'asistencia': asi,'alumno': al}   

class Porcentaje(LoginMixin,ListView):
    model = PromedioAsistencia    
    second_model = Asistencia
    template_name = 'institucion/materia/porcentaje.html'
    
    def get_context_data(self,**kwargs):#le doy el valor del id de la materia que seleccion
        context = super().get_context_data(**kwargs)#llamo a todos lo kwargs
        #context["promedioasistencia"] = self.model.objects.all()#guardo el valor de materia con el id seleccionado
        #context["asistencias"] = self.second_model.objects.all()
        b = self.model.objects.all()
        a = self.second_model.objects.all()
        for x in range(len(a)):#asistencia   
                   
            for i in range(len(b)):#promedioAsistencia
                if a[x].id_materia == b[i].id_materia and a[x].id_alumno == b[i].id_alumno:
                    b[i].dias = 0
                    if a[x].asistencia == "Presente":
                        b[i].dias_p = 0
                    b[i].total_d=0 
                    b[i].promedio= 100

        for x in range(len(a)):#asistencia   
                   
            for i in range(len(b)):#promedioAsistencia
                if a[x].id_materia == b[i].id_materia and a[x].id_alumno == b[i].id_alumno:
                    b[i].dias = b[i].dias + 1
                    if a[x].asistencia == "Presente":
                        b[i].dias_p = b[i].dias_p + 1 
                    b[i].total_d=b[i].dias_p/b[i].dias 
                    b[i].promedio= 100* b[i].total_d
                #c=b[i].dias_p/b[i].dias     
                  
                b[i].save()                              
        return {'PromedioAsistencia': b}

  
class ListadoPromedioAsistencia(LoginYSuperStaffMixin, ValidarPermisosMixin,ListView):
    model = PromedioAsistencia
    permission_required = ('institucion.view_promedioasistencia', 'institucion.add_promedioasistencia',
                           'institucion.delete_promedioasistencia', 'institucion.change_promedioasistencia')

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['promedioasistencias'] = self.get_queryset() #agregamos la consulta al contexto
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json',self.get_queryset()), 'application/json')
        else:
            return redirect('institucion:inicio_promedioasistencia')
 
#100 %   10 dias  8 dias de presente
# 8/10=0.8 ,  100*0.8=80