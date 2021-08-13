import json
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
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
    permission_required = ('libro.view_horario', 'libro.add_horario',
                           'libro.delete_horario', 'libro.change_horario')  

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
    permission_required = ('libro.view_horario', 'libro.add_horario',
                           'libro.delete_horario', 'libro.change_horario')
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
    permission_required = ('libro.view_horario', 'libro.add_horario',
                           'libro.delete_horario', 'libro.change_horario')

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
    permission_required  = ( 'libro.view_horario' , 'libro.add_horario' ,
                           'libro.delete_horario' , 'libro.change_horario' )

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
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno')  

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
    permission_required = ('libro.view_alumno', 'libro.add_alumno',
                           'libro.delete_alumno', 'libro.change_alumno')
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
    permission_required  = ( 'libro.view_alumno' , 'libro.add_alumno' ,
                           'libro.delete_alumno' , 'libro.change_alumno' )

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
    permission_required = ('libro.view_inscripcion', 'libro.add_inscripcion',
                           'libro.delete_inscripcion', 'libro.change_inscripcion')  

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

class ActualizarInscripcion(LoginYSuperStaffMixin, ValidarPermisosMixin,UpdateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = 'institucion/inscripcion/inscripcion.html'
    permission_required = ('libro.view_inscripcion', 'libro.add_inscripcion',
                           'libro.delete_inscripcion', 'libro.change_inscripcion')
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
    template_name = 'institucion/inscripcion/crear_inscripcion.html'
    permission_required = ('libro.view_inscripcion', 'libro.add_inscripcion',
                           'libro.delete_inscripcion', 'libro.change_inscripcion')

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
            return  redirect ( 'institucion: inicio_inscripcion' )

class EliminarInscripcion(LoginYSuperStaffMixin, ValidarPermisosMixin,DeleteView):
    model = Inscripcion
    template_name = 'institucion/inscripcion/eliminar_inscripcion.html'
    permission_required  = ( 'libro.view_inscripcion' , 'libro.add_inscripcion' ,
                           'libro.delete_inscripcion' , 'libro.change_inscripcion' )

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

class ListadoProfesores(LoginYSuperStaffMixin, ValidarPermisosMixin,View):
    model = Profesor
    permission_required = ('libro.view_profesor', 'libro.add_profesor',
                           'libro.delete_profesor', 'libro.change_profesor')  

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
    permission_required = ('libro.view_profesor', 'libro.add_profesor',
                           'libro.delete_profesor', 'libro.change_profesor')
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
    permission_required = ('libro.view_profesor', 'libro.add_profesor',
                           'libro.delete_profesor', 'libro.change_profesor')

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
    permission_required  = ( 'libro.view_profesor' , 'libro.add_profesor' ,
                           'libro.delete_profesor' , 'libro.change_profesor' )

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
    permission_required = ('libro.view_materia', 'libro.add_materia',
                           'libro.delete_materia', 'libro.change_materia')  

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
    permission_required = ('libro.view_materia', 'libro.add_materia',
                           'libro.delete_materia', 'libro.change_materia')
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
    permission_required = ('libro.view_materia', 'libro.add_materia',
                           'libro.delete_materia', 'libro.change_materia')

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
    permission_required  = ( 'libro.view_materia' , 'libro.add_materia' ,
                           'libro.delete_materia' , 'libro.change_materia' )

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
    permission_required = ('libro.view_notas', 'libro.add_notas',
                           'libro.delete_notas', 'libro.change_notas')  

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
    permission_required = ('libro.view_notas', 'libro.add_notas',
                           'libro.delete_notas', 'libro.change_notas')
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
    permission_required = ('libro.view_notas', 'libro.add_notas',
                           'libro.delete_notas', 'libro.change_notas')

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
    permission_required  = ( 'libro.view_notas' , 'libro.add_notas' ,
                           'libro.delete_notas' , 'libro.change_notas' )

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
    permission_required = ('libro.view_carrera', 'libro.add_carrera',
                           'libro.delete_carrera', 'libro.change_carrera')  

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
    permission_required = ('libro.view_carrera', 'libro.add_carrera',
                           'libro.delete_carrera', 'libro.change_carrera')
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
    permission_required = ('libro.view_carrera', 'libro.add_carrera',
                           'libro.delete_carrera', 'libro.change_carrera')

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
    permission_required  = ( 'libro.view_carrera' , 'libro.add_carrera' ,
                           'libro.delete_carrera' , 'libro.change_carrera' )

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
