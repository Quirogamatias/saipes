import json
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse, request
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView,DetailView
from apps.usuario.mixins import LoginYSuperStaffMixin,ValidarPermisosMixin,LoginMixin,ValidarAlumno,ValidarAdministrador,ValidarProfesor
from apps.usuario.models import Usuario
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from apps.usuario.models import Usuario
from apps.usuario.forms import FormularioUsuario
#from django.test import TestForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


class Inicio(TemplateView):
    template_name = 'index.html'

class InicioAdministrador(ValidarAdministrador, TemplateView):
    template_name = 'institucion/administrador/listar_administrador.html'
    permission_required = ('institucion.view_administrador', 'institucion.add_administrador',
                           'institucion.delete_administrador', 'institucion.change_administrador')

class InicioAdministradores(ValidarAdministrador, TemplateView):
    template_name = 'institucion/administrador/estado_administrador.html'
    permission_required = ('institucion.view_administrador', 'institucion.add_administrador',
                           'institucion.delete_administrador', 'institucion.change_administrador')

class InicioPromedioAsistencia(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/porcentaje/listar_porcentaje.html'
    permission_required = ('institucion.view_promedioasistencia', 'institucion.add_promedioasistencia',
                           'institucion.delete_promedioasistencia', 'institucion.change_promedioasistencia')

class InicioPromedioNotasFinal(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/porcentaje/promedio_notas.html'
    permission_required = ('institucion.view_promedionotasfinal', 'institucion.add_promedionotasfinal',
                           'institucion.delete_promedionotasfinal', 'institucion.change_promedionotasfinal')

class InicioPromedioNotasParcial(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/porcentaje/promedio_notasp.html'
    permission_required = ('institucion.view_promedionotasparcial', 'institucion.add_promedionotasparcial',
                           'institucion.delete_promedionotasparcial', 'institucion.change_promedionotasparcial')

class InicioCurso(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/curso/listar_curso.html'
    permission_required = ('institucion.view_curso', 'institucion.add_curso',
                           'institucion.delete_curso', 'institucion.change_curso')

class InicioAlumno(ValidarAlumno, TemplateView):
    template_name = 'institucion/alumno/listar_alumno.html'
    permission_required = ('institucion.view_alumno', 'institucion.add_alumno',
                           'institucion.delete_alumno', 'institucion.change_alumno')

class InicioAlumnos(ValidarAlumno, TemplateView):
    template_name = 'institucion/alumno/estado_alumno.html'
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
    
class InicioInscripcionProfesor(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/inscripcionprofesor/listar_inscripcion_profesores.html'
    permission_required = ('institucion.view_inscripcionprofesor', 'institucion.add_inscripcionprofesor',
                           'institucion.delete_inscripcionprofesor', 'institucion.change_inscripcionprofesor')

class InicioInscripcionExamen(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/inscripcionexamen/listar_inscripcion_examenes.html'
    permission_required = ('institucion.view_inscripcionexamenr', 'institucion.add_inscripcionexamen',
                           'institucion.delete_inscripcionexamen', 'institucion.change_inscripcionexamen')

class InicioMateria(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/materia/listar_materia.html'
    permission_required = ('institucion.view_materia', 'institucion.add_materia',
                           'institucion.delete_materia', 'institucion.change_materia')

class InicioNotas(LoginYSuperStaffMixin, ValidarPermisosMixin, TemplateView):
    template_name = 'institucion/notas/listar_notas.html'
    permission_required = ('institucion.view_notas', 'institucion.add_notas',
                           'institucion.delete_notas', 'institucion.change_notas')

class InicioProfesor(ValidarProfesor, TemplateView):
    template_name = 'institucion/profesor/listar_profesor.html'
    permission_required = ('institucion.view_profesor', 'institucion.add_profesor',
                           'institucion.delete_profesor', 'institucion.change_profesor')

class InicioProfesores(ValidarProfesor, TemplateView):
    template_name = 'institucion/profesor/estado_profesor.html'
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
        a=0
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo = Curso(
                    nombre = form.cleaned_data.get('nombre'),
                    capacidad = form.cleaned_data.get('capacidad'),
                    turno = form.cleaned_data.get('turno')
                )
                curso = self.model.objects.all()               
                
                for i in range(len(curso)):
                    if curso[i].estado == True:
                        if curso[i].nombre==nuevo.nombre:
                            if curso[i].turno==nuevo.turno:
                                a=1
                                mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe!'
                                error = form.errors
                                response = JsonResponse({'mensaje':mensaje,'error':error})
                                response.status_code = 400
                                return response
                                
                if a==0:
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
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            if form.is_valid():
                nuevo= Horario(
                    dia=form.cleaned_data.get('dia'),
                    hora_inicio=form.cleaned_data.get('hora_inicio'),
                    hora_fin=form.cleaned_data.get('hora_fin'),
                    id_curso=form.cleaned_data.get('id_curso')
                )#con esto guardo los datos recientes en la variable nuevo y lo uso normalmente
                
                horario = self.model.objects.all()               
                
                for i in range(len(horario)):
                    if horario[i].estado == True:
                        if horario[i].id_curso==nuevo.id_curso:
                            if horario[i].dia==nuevo.dia:
                                if horario[i].hora_inicio==nuevo.hora_inicio:
                                    a=1
                                    mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe!'
                                    error = form.errors
                                    response = JsonResponse({'mensaje':mensaje,'error':error})
                                    response.status_code = 400
                                    return response
                                
                if a==0:
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

class ListadoAlumnos(ValidarAlumno,View):
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
    second_model = Profesor
    form_class = AlumnoForm
    third_model = Usuario
    third_form_class = FormularioUsuario
    fourth_model = Administrador
    fourth_form_class = AdministradorForm
    template_name = 'institucion/alumno/crear_alumno.html'
    permission_required = ('institucion.view_alumno', 'institucion.add_alumno',
                           'institucion.delete_alumno', 'institucion.change_alumno')
    
    def get_context_data(self, **kwargs):
        context = super(CrearAlumno, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.third_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            form2 = self.third_form_class(data = request.POST,files = request.FILES)
            if form.is_valid() and form2.is_valid():
                nuevo= Alumno(
                    dni=form.cleaned_data.get('dni'),
                    email=form.cleaned_data.get('email'),                    
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido')                                       
                )

                alumno = self.model.objects.all()
                profesor = self.second_model.objects.all()
                usuario = self.third_model.objects.all()
                administrador = self.fourth_model.objects.all()

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.dni == alumno[j].dni or nuevo.email == alumno[j].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.dni == profesor[i].dni or nuevo.email == profesor[i].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response                

                if a==0:
                    form.save()
                    form2.save()    

                    alum = self.model.objects.all()
                    usua = self.third_model.objects.all()
                    for j in range(len(usua)):
                        if usua[j].is_active == True:
                            if nuevo.email == usua[j].email:
                                for i in range(len(alum)):
                                    if alum[i].estado == True:                                                       
                                        if nuevo.email == alum[i].email:
                                            alum[i].id_usuario = usua[j]
                                            alum[i].notificacion = True
                                            usua[j].tipo = 'Alumno'  
                                            usua[j].save()                                       
                                            alum[i].save()                                          
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
    third_form_class = PromedioNotasFinalForm
    fourth_form_class = PromedioNotasParcialForm
    template_name = 'institucion/inscripcion/crear_inscripcion.html'
    permission_required = ('institucion.view_inscripcion', 'institucion.add_inscripcion',
                           'institucion.delete_inscripcion', 'institucion.change_inscripcion')

    def get_context_data(self, **kwargs):
        context = super(CrearInscripcion, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        if 'form4' not in context:
            context['form4'] = self.fourth_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            form2 = self.second_form_class(data = request.POST,files = request.FILES)
            form3 = self.third_form_class(data = request.POST,files = request.FILES)
            form4 = self.fourth_form_class(data = request.POST,files = request.FILES)
            if form.is_valid() and form2.is_valid() and form3.is_valid():
                nuevo= Inscripcion(
                    id_alumno=form.cleaned_data.get('id_alumno'),
                    id_materia=form.cleaned_data.get('id_materia')
                )

                inscripcion = self.model.objects.all()

                for i in range(len(inscripcion)):
                    if inscripcion[i].estado == True:
                        if inscripcion[i].id_alumno == nuevo.id_alumno and inscripcion[i].id_materia == nuevo.id_materia:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque el alumno ya se inscribio a esa materia!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
               
                if a==0:
                    form.save()
                    form2.save()
                    form3.save()
                    form4.save()
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

class ListadoAdministradores(ValidarAdministrador,ListView):

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
    second_model = Alumno
    third_model = Profesor
    #second_form_class = AlumnoForm
    fourth_model = Usuario
    fourth_form_class = FormularioUsuario
    template_name = 'institucion/administrador/crear_administrador.html'
    permission_required = ('institucion.view_administrador', 'institucion.add_administrador',
                           'institucion.delete_administrador', 'institucion.change_administrador')
    
    def get_context_data(self, **kwargs):
        context = super(CrearAdministrador, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.fourth_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            form2 = self.fourth_form_class(data = request.POST,files = request.FILES)         
            if form.is_valid() and form2.is_valid():
                nuevo = Administrador(
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido'),
                    telefono=form.cleaned_data.get('telefono'),
                    domicilio=form.cleaned_data.get('domicilio'),
                    email=form.cleaned_data.get('email')
                )
                administrador = self.model.objects.all()
                alumno = self.second_model.objects.all()
                profesor = self.third_model.objects.all()
                #usuario = self.third_model.objects.all()

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.email == alumno[j].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.email == profesor[i].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
                if a==0:
                    form.save()
                    form2.save()    

                    admin = self.model.objects.all()
                    usua = self.fourth_model.objects.all()
                    for j in range(len(usua)):
                        if usua[j].is_active == True:
                            if nuevo.email == usua[j].email:
                                for i in range(len(admin)):
                                    if admin[i].estado == True:                                                       
                                        if nuevo.email == admin[i].email:
                                            admin[i].id_usuario = usua[j]
                                            admin[i].notificacion = True
                                            usua[j].tipo = 'Administrador'  
                                            usua[j].save()                                       
                                            admin[i].save()                                          
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

class ListadoProfesores(ValidarProfesor,ListView):
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
    second_model = Alumno
    form_class = ProfesorForm
    third_model = Usuario
    third_form_class = FormularioUsuario
    fourth_model = Administrador
    fourth_form_class = AdministradorForm
    template_name = 'institucion/profesor/crear_profesor.html'
    permission_required = ('institucion.view_profesor', 'institucion.add_profesor',
                           'institucion.delete_profesor', 'institucion.change_profesor')
    

    def get_context_data(self, **kwargs):
        context = super(CrearProfesor, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.third_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            form2 = self.third_form_class(data = request.POST,files = request.FILES)
            if form.is_valid() and form2.is_valid():
                nuevo= Profesor(
                    dni=form.cleaned_data.get('dni'),
                    email=form.cleaned_data.get('email')
                )

                profesor = self.model.objects.all()
                alumno = self.second_model.objects.all()
                administrador = self.fourth_model.objects.all()

                for k in range(len(administrador)):
                    if administrador[k].estado == True:
                        if nuevo.email == administrador[k].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for i in range(len(profesor)):
                    if profesor[i].estado == True:
                        if nuevo.dni == profesor[i].dni or nuevo.email == profesor[i].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response

                for j in range(len(alumno)):
                    if alumno[j].estado == True:
                        if nuevo.dni == alumno[j].dni or nuevo.email == alumno[j].email:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe un usuario con ese DNI o Email!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
               
                if a==0:
                    form.save()
                    form2.save()    

                    prof = self.model.objects.all()
                    usua = self.third_model.objects.all()
                    for j in range(len(usua)):
                        if usua[j].is_active == True:
                            if nuevo.email == usua[j].email:
                                for i in range(len(prof)):
                                    if prof[i].estado == True:                                                       
                                        if nuevo.email == prof[i].email:
                                            prof[i].id_usuario = usua[j]
                                            prof[i].notificacion = True
                                            usua[j].tipo = 'Profesor'  
                                            usua[j].save()                                       
                                            prof[i].save()                                          
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
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            if form.is_valid():
                nuevo= Materia(
                    materia=form.cleaned_data.get('materia')
                )#con esto guardo los datos recientes en la variable nuevo y lo uso normalmente
                
                materia = self.model.objects.all()               
                
                for i in range(len(materia)):
                    if materia[i].estado == True:
                        if materia[i].materia==nuevo.materia:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
                                
                if a==0:
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
    second_model = PromedioNotasFinal
    third_model = PromedioNotasParcial
    form_class = NotasForm
    second_form_class = PromedioNotasFinalForm
    third_form_class = PromedioNotasParcialForm
    fourth_model = Inscripcion
    template_name = 'institucion/notas/crear_notas.html'
    permission_required = ('institucion.view_notas', 'institucion.add_notas',
                           'institucion.delete_notas', 'institucion.change_notas')

    def post(self,request,*args,**kwargs):        
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            if form.is_valid():
                #a = form.cleaned_data['id_materia']
                #b = form.cleaned_data['id_alumno']
                #c = form.cleaned_data['tipo']
                nuevo= Notas(
                    notas=form.cleaned_data.get('notas'),
                    id_materia=form.cleaned_data.get('id_materia'),
                    id_alumno=form.cleaned_data.get('id_alumno'),
                    tipo=form.cleaned_data.get('tipo')
                )#con esto guardo los datos recientes en la variable nuevo y lo uso normalmente
                
                promedioF = self.second_model.objects.all()
                promedioP = self.third_model.objects.all()
                inscripcion = self.fourth_model.objects.all()                
                
                if nuevo.notas >= 0 and nuevo.notas <=10:
                    if nuevo.tipo == "Final":
                        for i in range(len(promedioF)):
                            if promedioF[i].estado==True:
                                if nuevo.id_materia == promedioF[i].id_materia and nuevo.id_alumno == promedioF[i].id_alumno:
                                    if promedioF[i].cantidad < 4:
                                        promedioF[i].cantidad = promedioF[i].cantidad + 1
                                        promedioF[i].suma = promedioF[i].suma + nuevo.notas
                                        promedioF[i].total=promedioF[i].suma / promedioF[i].cantidad
                                        form.save() 
                                        promedioF[i].save()
                                        mensaje = f'{self.model.__name__} registrado correctamente!'
                                        error = 'No hay error!'
                                        response = JsonResponse({'mensaje':mensaje,'error':error})
                                        response.status_code = 201
                                        return response
                                    else:
                                        mensaje = f'{self.model.__name__} no se ha podido registrar, porque ya registro las 4 notas del final!'
                                        error = form.errors
                                        response = JsonResponse({'mensaje':mensaje,'error':error})
                                        response.status_code = 400
                                        return response
                    
                    if nuevo.tipo == "Parcial":
                        for i in range(len(promedioP)):
                            if promedioP[i].estado==True:
                                if nuevo.id_materia == promedioP[i].id_materia and nuevo.id_alumno == promedioP[i].id_alumno:                       
                                    if promedioP[i].cantidad < 2:
                                        promedioP[i].cantidad = promedioP[i].cantidad + 1
                                        promedioP[i].suma = promedioP[i].suma + nuevo.notas
                                        promedioP[i].total=promedioP[i].suma / promedioP[i].cantidad
                                        form.save() 
                                        promedioP[i].save()
                                        mensaje = f'{self.model.__name__} registrado correctamente!'
                                        error = 'No hay error!'
                                        response = JsonResponse({'mensaje':mensaje,'error':error})
                                        response.status_code = 201
                                        return response
                                    else:
                                        mensaje = f'{self.model.__name__} no se ha podido registrar, porque ya ingreso las 2 notas de parcial!'
                                        error = form.errors
                                        response = JsonResponse({'mensaje':mensaje,'error':error})
                                        response.status_code = 400
                                        return response

                    a=0  
                    for i in range(len(inscripcion)):
                        if inscripcion[i].id_alumno == nuevo.id_alumno and inscripcion[i].id_materia == nuevo.id_materia:
                            a=1

                    if a==0:
                        mensaje = f'{self.model.__name__} no se ha podido registrar, porque el alumno no esta inscripto a esta materia!'
                        error = form.errors
                        response = JsonResponse({'mensaje':mensaje,'error':error})
                        response.status_code = 400
                        return response
                else:
                    mensaje = f'{self.model.__name__} no se ha podido registrar, porque la nota tiene que ser mayor o igual de 0 y menor o igual de 10!'
                    error = form.errors
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 400
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
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            if form.is_valid():
                nuevo= Carrera(
                    carrera=form.cleaned_data.get('carrera')
                )#con esto guardo los datos recientes en la variable nuevo y lo uso normalmente
                
                carrera = self.model.objects.all()               
                
                for i in range(len(carrera)):
                    if carrera[i].estado == True:
                        if carrera[i].carrera == nuevo.carrera:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque ya existe!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
                                
                if a==0:
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
    second_model = PromedioAsistencia
    third_model = Inscripcion
    form_class = AsistenciaForm
    second_form_class = PromedioAsistenciaForm
    third_form_class = InscripcionForm
    template_name = 'institucion/asistencia/crear_asistencia.html'
    permission_required = ('institucion.view_asistencia', 'institucion.add_asistencia',
                           'institucion.delete_asistencia', 'institucion.change_asistencia')
    

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)           
            if form.is_valid():
                
                nuevo= Asistencia(
                    id_materia=form.cleaned_data.get('id_materia'),
                    id_alumno=form.cleaned_data.get('id_alumno'),
                    dia=form.cleaned_data.get('dia'),
                    asistencia=form.cleaned_data.get('asistencia')
                )  
                
                promedioasistencia = self.second_model.objects.all()  
                inscripcion = self.third_model.objects.all()   
                
                for i in range(len(promedioasistencia)):
                    if nuevo.id_materia == promedioasistencia[i].id_materia and nuevo.id_alumno == promedioasistencia[i].id_alumno:
                        promedioasistencia[i].dias = promedioasistencia[i].dias + 1
                        if nuevo.asistencia == "Presente":                            
                            promedioasistencia[i].dias_p = promedioasistencia[i].dias_p + 1 
                        promedioasistencia[i].total_d=promedioasistencia[i].dias_p/promedioasistencia[i].dias 
                        promedioasistencia[i].promedio= 100* promedioasistencia[i].total_d
                        promedioasistencia[i].save() 
                        form.save()
                        mensaje = f'{self.model.__name__} registrado correctamente!'
                        error = 'No hay error!'
                        response = JsonResponse({'mensaje':mensaje,'error':error})
                        response.status_code = 201
                        return response
                        
                a=0  
                for i in range(len(inscripcion)):
                    if inscripcion[i].id_alumno == nuevo.id_alumno and inscripcion[i].id_materia == nuevo.id_materia:
                        a=1

                if a==0:
                    mensaje = f'{self.model.__name__} no se ha podido registrar, porque el alumno no esta inscripto a esta materia!'
                    error = form.errors
                    response = JsonResponse({'mensaje':mensaje,'error':error})
                    response.status_code = 400
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
class ListadoPromedioNotasFinal(LoginYSuperStaffMixin, ValidarPermisosMixin,ListView):
    model = PromedioNotasFinal
    permission_required = ('institucion.view_promedionotasfinal', 'institucion.add_promedionotasfinal',
                           'institucion.delete_promedionotasfinal', 'institucion.change_promedionotasfinal')

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['promedionotasfinales'] = self.get_queryset() #agregamos la consulta al contexto
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json',self.get_queryset()), 'application/json')
        else:
            return redirect('institucion:InicioPromedioNotasFinal')
 
class ListadoPromedioNotasParcial(LoginYSuperStaffMixin, ValidarPermisosMixin,ListView):
    model = PromedioNotasParcial
    permission_required = ('institucion.view_promedionotasparcial', 'institucion.add_promedionotasparcial',
                           'institucion.delete_promedionotasparcial', 'institucion.change_promedionotasparcial')
    #queryset = PromedioNotasParcial.objects.order_by('-id_promedionotasparcial')
    #def post(self,request,*args,**kwargs):   
     #   promedioP = self.model.objects.all()
      #  promedioPa = self.model.objects.all()

        #author_count = self.model.objects.count()
        #cut_off_score = self.model.objects.order_by('-total').values_list('total')[min(30, author_count)]
        #top_authors = self.model.objects.filter(total__gte=cut_off_score).order_by('total')
      
    def get_queryset(self):
        return self.model.objects.filter(estado = True) 

    def get_context_data(self,**kwargs):
        #orden = PromedioNotasParcial.objects.all().order_by('total')
        #return redirect('institucion:InicioPromedioNotasParcial',{"PromedioNotasParcial": orden})

        contexto= {}
        contexto ['promedionotasparciales'] = self.get_queryset() #agregamos la consulta al contexto
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json',self.get_queryset()), 'application/json')
        else:
            return redirect('institucion:InicioPromedioNotasParcial')

def formularioContacto(request):
    return render(request,'institucion/mensaje/formularioContacto.html')

def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + "/ Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = "sistema.academico.ipes@gmail.com",request.POST["txtEmail"]
        send_mail(asunto,mensaje,email_desde,email_para, fail_silently=False)
        return render(request,'institucion/mensaje/contactoExitoso.html')
    return render(request,'institucion/mensaje/formularioContacto.html')

class EnviarMensaje(LoginYSuperStaffMixin, ValidarPermisosMixin,ListView):
    template_name = 'institucion/mensaje/enviar_mensaje.html'
    model = Alumno
    #second_model = PromedioNotasFinal
    #third_model = PromedioNotasParcial
    #form_class = AlumnoForm
    #second_form_class = PromedioNotasFinalForm
    #third_form_class = PromedioNotasParcialForm
    #fourth_model = Inscripcion
    

    def post(self,request,*args,**kwargs):  
        alumno = self.model.objects.all() 
        if request.method == "POST":
            asunto = request.POST["txtAsunto"]
            mensaje = request.POST["txtMensaje"]
            email_desde = settings.EMAIL_HOST_USER
            #email_para = "sistema.academico.ipes@gmail.com",request.POST["txtEmail"]
         
                
            #alumno = self.model.objects.all()               
                
        for i in range(len(alumno)):
            if alumno[i].estado == True:
                email_para= "sistema.academico.ipes@gmail.com",alumno[i].email
                send_mail(asunto,mensaje,email_desde,email_para, fail_silently=False)
                    #mensaje = f'{self.model.__name__} mensaje enviado correctamente!'
                    #error = 'No hay error!'
                    #response = JsonResponse({'mensaje':mensaje,'error':error})
                    #response.status_code = 201
                    #return response
                    #llamar a los mail de alumno y ponerlo en una variable email_para, esto es en un ciclo para enviar el mensaje a varios usuarios a la vez
                    #en el if tendria que prenguntar si el alumno acepta recibir mensjae, de advertencia
        
        return render(request,'institucion/mensaje/enviar_mensaje.html')            
           
        #else:
         #   return  redirect ( 'institucion: inicio_alumno' )

#eliminar atributo id materia de profesor, crear una clase que diga inscricpion de porfesor, en donde tiene el id de materia,id de profesor, curso
#registrar inscripcion a examen final con 2 dias de anticipacion

class CrearInscripcionProfesor(LoginYSuperStaffMixin, ValidarPermisosMixin,CreateView):
    model = InscripcionProfesor
    form_class = InscripcionProfesorForm
    template_name = 'institucion/inscripcionprofesor/crear_inscripcion_profesor.html'
    permission_required = ('institucion.view_inscripcionprofesor', 'institucion.add_inscripcionprofesor',
                           'institucion.delete_inscripcionprofesor', 'institucion.change_inscripcionprofesor')

    def get_context_data(self, **kwargs):
        context = super(CrearInscripcionProfesor, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            if form.is_valid():
                nuevo= InscripcionProfesor(
                    id_profesor=form.cleaned_data.get('id_profesor'),
                    id_materia=form.cleaned_data.get('id_materia')
                )

                inscripcionprofesor = self.model.objects.all()

                for i in range(len(inscripcionprofesor)):
                    if inscripcionprofesor[i].estado == True:
                        if inscripcionprofesor[i].id_profesor == nuevo.id_profesor and inscripcionprofesor[i].id_materia == nuevo.id_materia:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar porque el profesor ya se inscribio a esa materia!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
               
                if a==0:
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
            return  redirect ( 'institucion: inicio_inscripcion_profesor' )

class ListadoInscripcionProfesores(LoginYSuperStaffMixin, ValidarPermisosMixin,View):
    model = InscripcionProfesor
    permission_required = ('institucion.view_inscripcionprofesor', 'institucion.add_inscripcionprofesor',
                           'institucion.delete_inscripcionprofesor', 'institucion.change_inscripcionprofesor')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['inscripcionprofesores'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_inscripcion_profesor')

class CrearInscripcionExamen(LoginYSuperStaffMixin, ValidarPermisosMixin,CreateView):
    model = InscripcionExamen
    form_class = InscripcionExamenForm
    second_model = Inscripcion
    second_form_class = InscripcionForm
    template_name = 'institucion/inscripcionexamen/crear_inscripcion_examen.html'
    permission_required = ('institucion.view_inscripcionexamen', 'institucion.add_inscripcionexamen',
                           'institucion.delete_inscripcionexamen', 'institucion.change_inscripcionexamen')

    def get_context_data(self, **kwargs):
        context = super(CrearInscripcionExamen, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        #if 'form2' not in context:
         #   context['form2'] = self.second_form_class(self.request.GET)    
        #return context
    
    #def get_queryset(self):
        
     #   return self.model.objects.filter(id_materia=self.request.user,estado = True)  


    def post(self,request,*args,**kwargs):
        a=0
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            if form.is_valid():
                nuevo= InscripcionExamen(
                    id_alumno=form.cleaned_data.get('id_alumno'),
                    id_materia=form.cleaned_data.get('id_materia')
                )

                inscripcionexamen = self.model.objects.all()

                for i in range(len(inscripcionexamen)):
                    if inscripcionexamen[i].estado == True:
                        if inscripcionexamen[i].id_alumno == nuevo.id_alumno and inscripcionexamen[i].id_materia == nuevo.id_materia:
                            a=1
                            mensaje = f'{self.model.__name__} no se ha podido registrar el alumno al examen porque ya se inscribio a es examen!'
                            error = form.errors
                            response = JsonResponse({'mensaje':mensaje,'error':error})
                            response.status_code = 400
                            return response
               
                if a==0:
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
            return  redirect ( 'institucion: inicio_inscripcion_examen' )

class ListadoInscripcionExamenes(LoginYSuperStaffMixin, ValidarPermisosMixin,View):
    model = InscripcionExamen
    permission_required = ('institucion.view_inscripcionexamen', 'institucion.add_inscripcionexamen',
                           'institucion.delete_inscripcionexamen', 'institucion.change_inscripcionexamen')  

    def get_queryset(self):
        return self.model.objects.filter(estado = True)  

    def get_context_data(self,**kwargs):
        contexto= {}
        contexto ['inscripcionexamenes'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_inscripcion_examen')

class EstadoAlumno(ValidarAlumno,View):
    model = Alumno
    #second_model = Usuario
    permission_required = ('institucion.view_alumno', 'institucion.add_alumno',
                           'institucion.delete_alumno', 'institucion.change_alumno')  
    
    def get_queryset(self):
        return self.model.objects.filter(id_usuario=self.request.user,estado = True)  

    def get_context_data(self):
        pk = self.kwargs.get('pk')
        alumno = self.model.objects.get(pk= pk)
        return alumno

    
    #def get_context_data(self,**kwargs):
     #   contexto= {}
      #  contexto ['alumnos'] = self.get_queryset()
       # contexto['form'] = self.form_class
        #return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_alumnos')

class EstadoProfesor(ValidarProfesor,View):
    model =Profesor
    permission_required = ('institucion.view_profesor', 'institucion.add_profesor',
                           'institucion.delete_profesor', 'institucion.change_profesor')  
    
    def get_queryset(self):
        return self.model.objects.filter(id_usuario=self.request.user,estado = True)  

    def get_context_data(self):
        pk = self.kwargs.get('pk')
        profesor = self.model.objects.get(pk= pk)
        return profesor

    
    #def get_context_data(self,**kwargs):
     #   contexto= {}
      #  contexto ['alumnos'] = self.get_queryset()
       # contexto['form'] = self.form_class
        #return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_profesores')

class EstadoAdministrador(ValidarAdministrador,View):

    model = Administrador
    #second_model = Usuario
    permission_required = ('institucion.view_administrador', 'institucion.add_administrador',
                           'institucion.delete_administrador', 'institucion.change_administrador')  
    
    def get_queryset(self):
        return self.model.objects.filter(id_usuario=self.request.user,estado = True)  

    def get_context_data(self):
        pk = self.kwargs.get('pk')
        administrador = self.model.objects.get(pk= pk)
        return administrador

    
    #def get_context_data(self,**kwargs):
     #   contexto= {}
      #  contexto ['alumnos'] = self.get_queryset()
       # contexto['form'] = self.form_class
        #return contexto
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():            
            return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')
        else:
            return redirect('institucion:inicio_administradores')


class TestView(LoginYSuperStaffMixin, ValidarPermisosMixin,TemplateView):
    model = Materia
    second_model = Carrera
    template_name = "institucion/inscripcionexamen/test.html"

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, ** kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_carrera_id':           
                #pass
                data =[]
                materia = self.model.objects.all()
                carrera = Carrera.objects.filter(id_carrera=request.POST['id'])
                #for j in range(len(materia)):
                 #   if materia[j].id_materia == carrera.obtener_materias:
                #data.append(carrera.obtener_materias)
                

                for i in Carrera.objects.filter(id_carrera=request.POST['id']):
                    for materia in i.id_materia.all():
                    #if i.id_materia
                 #   for j in range(len(materia)):
                  #      materia[j].id_materia == 
                        data.append({'id':materia.id_materia, 'materia':materia.materia})
                  #tengo que saber que datos me llega en este caso el id de carrera, como lo relaciono con el de materia             
            else:
                data['error'] = 'ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Select animado | Django'
        context['form'] = TestForm()#self.TestForm()#self.TestForm(form)#self.TestForm()#self.form_class 
        return context
    
