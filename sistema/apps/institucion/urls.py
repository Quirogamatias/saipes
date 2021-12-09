from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('formularioContacto/',login_required(formularioContacto),name = 'formularioContacto'),
    path('contactar/',login_required(contactar),name = 'contactar'),
    path('enviar_mensaje/',login_required(EnviarMensaje.as_view()),name = 'enviar_mensaje'),
    path('mensaje/<int:pk>/',login_required(Mensaje.as_view()),name = 'mensaje'),
    path('mensajead/<int:pk>/',login_required(MensajeAd.as_view()),name = 'mensajead'),
    path('mensajea/<int:pk>/',login_required(MensajeA.as_view()),name = 'mensajea'),
    path('mensajeal/<int:pk>/',login_required(MensajeAl.as_view()),name = 'mensajeal'),
    path('mensaje_advertencia/',login_required(MensajeAdvertencia.as_view()),name = 'mensaje_advertencia'),
    path('mensaje_advertencia_asistencia/',login_required(MensajeAdvertenciaAsistencia.as_view()),name = 'mensaje_advertencia_asistencia'),
    
    path('inicio_administrador/',InicioAdministrador.as_view(), name = 'inicio_administrador'),
    #path('inicio_administradores/',InicioAdministradores.as_view(), name = 'inicio_administradores'),
    path('inicio_curso/',InicioCurso.as_view(), name = 'inicio_curso'),
    path('inicio_alumno/',InicioAlumno.as_view(), name = 'inicio_alumno'),
    path('inicio_alumnop/',InicioAlumnop.as_view(), name = 'inicio_alumnop'),
    path('inicio_alumnos/',InicioAlumnos.as_view(), name = 'inicio_alumnos'),
    path('inicio_carrera/',InicioCarrera.as_view(), name = 'inicio_carrera'),
    path('inicio_horario/',InicioHorario.as_view(), name = 'inicio_horario'),
    path('inicio_horariot/',InicioHorariot.as_view(), name = 'inicio_horariot'),
    path('inicio_inscripcion/',InicioInscripcion.as_view(), name = 'inicio_inscripcion'),
    path('inicio_inscripcion_profesor/',InicioInscripcionProfesor.as_view(), name = 'inicio_inscripcion_profesor'),
    path('inicio_inscripcion_examen/',InicioInscripcionExamen.as_view(), name = 'inicio_inscripcion_examen'),
    path('inicio_inscripcion_examen_alumno/',InicioInscripcionExamenAlumno.as_view(), name = 'inicio_inscripcion_examen_alumno'),
    path('inicio_materia/',InicioMateria.as_view(), name = 'inicio_materia'),
    path('inicio_materiat/',InicioMateriat.as_view(), name = 'inicio_materiat'),
    path('inicio_notas/',InicioNotas.as_view(), name = 'inicio_notas'),
    path('inicio_profesor/',InicioProfesor.as_view(), name = 'inicio_profesor'),
    path('inicio_profesort/',InicioProfesort.as_view(), name = 'inicio_profesort'),
    path('inicio_profesoral/',InicioProfesorAl.as_view(), name = 'inicio_profesoral'),
    path('inicio_profesores/',InicioProfesores.as_view(), name = 'inicio_profesores'),
    path('inicio_asistencia/',InicioAsistencia.as_view(), name = 'inicio_asistencia'),
    path('inicio_fecha/',InicioFecha.as_view(), name = 'inicio_fecha'),
    path('inicio_promedioasistencia/',InicioPromedioAsistencia.as_view(), name = 'inicio_promedioasistencia'),
    path('inicio_promedionotasfinal/',InicioPromedioNotasFinal.as_view(), name = 'inicio_promedionotasfinal'),
    path('inicio_promedionotasparcial/',InicioPromedioNotasParcial.as_view(), name = 'inicio_promedionotasparcial'),
    path('Inicio_PromedioAsistenciaAlumno/',InicioPromedioAsistenciaAlumno.as_view(), name = 'Inicio_PromedioAsistenciaAlumno'),

    path('crear_curso/',login_required(CrearCurso.as_view()), name = 'crear_curso'),
    path('crear_horario/',login_required(CrearHorario.as_view()), name = 'crear_horario'),
    path('crear_alumno/',login_required(CrearAlumno.as_view()), name = 'crear_alumno'),
    path('crear_inscripcion/',login_required(CrearInscripcion.as_view()), name = 'crear_inscripcion'),
    path('crear_inscripcion_profesor/',login_required(CrearInscripcionProfesor.as_view()), name = 'crear_inscripcion_profesor'),
    path('crear_inscripcion_examen/',login_required(CrearInscripcionExamen.as_view()), name = 'crear_inscripcion_examen'),
    path('crear_inscripcion_examen_alumno/',login_required(CrearInscripcionExamenAlumno.as_view()), name = 'crear_inscripcion_examen_alumno'),
    path('crear_administrador/',login_required(CrearAdministrador.as_view()), name = 'crear_administrador'),
    path('crear_profesor/',login_required(CrearProfesor.as_view()), name = 'crear_profesor'),
    path('crear_materia/',login_required(CrearMateria.as_view()), name = 'crear_materia'),
    path('crear_notas/',login_required(CrearNotas.as_view()), name = 'crear_notas'),
    path('crear_carrera/',login_required(CrearCarrera.as_view()), name = 'crear_carrera'),
    path('crear_asistencia/',login_required(CrearAsistencia.as_view()), name = 'crear_asistencia'),
    path('crear_fecha/',login_required(CrearFecha.as_view()), name = 'crear_fecha'),
    
    path('listar_cursos/',login_required(ListadoCursos.as_view()),name = 'listado_cursos'),
    path('listar_horarios/',login_required(ListadoHorarios.as_view()),name = 'listado_horarios'),
    path('listar_horariot/',login_required(ListadoHorariost.as_view()),name = 'listado_horariot'),
    path('listar_alumnos/',login_required(ListadoAlumnos.as_view()),name = 'listado_alumnos'),
    path('estado_alumno/',login_required(EstadoAlumno.as_view()),name = 'estado_alumno'),
    path('listar_alumnop/',login_required(ListadoAlumnop.as_view()),name = 'listado_alumnop'),
    path('listar_inscripciones/',login_required(ListadoInscripciones.as_view()),name = 'listado_inscripciones'),
    path('listar_inscripcion_profesores/',login_required(ListadoInscripcionProfesores.as_view()),name = 'listado_inscripcion_profesores'),
    path('listar_inscripcion_examenes/',login_required(ListadoInscripcionExamenes.as_view()),name = 'listado_inscripcion_examenes'),
    path('listar_inscripcion_examenes_alumno/',login_required(ListadoInscripcionExamenesAlumno.as_view()),name = 'listado_inscripcion_examenes_alumno'),
    path('listar_administradores/',login_required(ListadoAdministradores.as_view()),name = 'listado_administradores'),
    #path('estado_administrador/',login_required(EstadoAdministrador.as_view()),name = 'estado_administrador'),
    path('listar_profesorest/',login_required(ListadoProfesorest.as_view()),name = 'listado_profesorest'),
    path('listar_profesoresal/',login_required(ListadoProfesoresal.as_view()),name = 'listado_profesoresal'),
    path('listar_profesores/',login_required(ListadoProfesores.as_view()),name = 'listado_profesores'),
    path('estado_profesor/',login_required(EstadoProfesor.as_view()),name = 'estado_profesor'),
    path('listar_materias/',login_required(ListadoMaterias.as_view()),name = 'listado_materias'),
    path('listar_materiast/',login_required(ListadoMateriast.as_view()),name = 'listado_materiast'),
    path('listar_notas/',login_required(ListadoNotas.as_view()),name = 'listado_notas'),
    path('listar_carreras/',login_required(ListadoCarreras.as_view()),name = 'listado_carreras'),
    path('listar_asistencias/',login_required(ListadoAsistencia.as_view()),name = 'listado_asistencias'),
    path('listar_fechas/',login_required(ListadoFecha.as_view()),name = 'listado_fechas'),
    path('listar_porcentajes/',login_required(ListadoPromedioAsistencia.as_view()),name = 'listado_porcentajes'),
    #path('porcentaje/',login_required(Porcentaje.as_view()),name = 'porcentaje'),
    path('listar_promediosf/',login_required(ListadoPromedioNotasFinal.as_view()),name = 'listado_promediosf'),
    path('listar_promediosp/',login_required(ListadoPromedioNotasParcial.as_view()),name = 'listado_promediosp'),
    path('promedio_asistencia_alumno/',login_required(PromedioAsistenciaAlumno.as_view()),name = 'promedio_asistencia_alumno'),
    path('promedio_notas_final_alumno/',login_required(PromedioNotasFinalAlumno.as_view()),name = 'promedio_notas_final_alumno'),
    path('promedio_notas_parcial_alumno/',login_required(PromedioNotasParcialAlumno.as_view()),name = 'promedio_notas_parcial_alumno'),
    #path('listar_promediosp2/',login_required(ListadoPromedioNotasParcial2),name = 'listado_promediosp2'),
   
    path('editar_curso/<int:pk>/',login_required(ActualizarCurso.as_view()),name = 'editar_curso'),
    path('editar_horario/<int:pk>/',login_required(ActualizarHorario.as_view()),name = 'editar_horario'),
    path('editar_alumno/<int:pk>/',login_required(ActualizarAlumno.as_view()),name = 'editar_alumno'),
    path('editar_alumno2/<int:pk>/',login_required(ActualizarAlumno2.as_view()),name = 'editar_alumno2'),
    path('editar_inscripcion/<int:pk>/',login_required(ActualizarInscripcion.as_view()),name = 'editar_inscripcion'),
    #path('editar_inscripcion_profesor/<int:pk>/',login_required(ActualizarInscripcionProfesor.as_view()),name = 'editar_inscripcion_profesor'),
    path('editar_administrador/<int:pk>/',login_required(ActualizarAdministrador.as_view()),name = 'editar_administrador'),
    path('editar_profesor/<int:pk>/',login_required(ActualizarProfesor.as_view()),name = 'editar_profesor'),
    path('editar_profesor2/<int:pk>/',login_required(ActualizarProfesor2.as_view()),name = 'editar_profesor2'),
    path('editar_materia/<int:pk>/',login_required(ActualizarMateria.as_view()),name = 'editar_materia'),
    path('editar_notas/<int:pk>/',login_required(ActualizarNotas.as_view()),name = 'editar_notas'),
    path('editar_carrera/<int:pk>/',login_required(ActualizarCarrera.as_view()),name = 'editar_carrera'),
    path('editar_asistencia/<int:pk>/',login_required(ActualizarAsistencia.as_view()),name = 'editar_asistencia'),
    path('editar_fecha/<int:pk>/',login_required(ActualizarFecha.as_view()),name = 'editar_fecha'),
    path('editar_inscripcion_profesor/<int:pk>/',login_required(ActualizarInscripcionProfesor.as_view()),name = 'editar_inscripcion_profesor'),
    path('editar_inscripcion_examen/<int:pk>/',login_required(ActualizarInscripcionExamen.as_view()),name = 'editar_inscripcion_examen'),
    
    path('eliminar_curso/<int:pk>/',login_required(EliminarCurso.as_view()),name = 'eliminar_curso'),
    path('eliminar_horario/<int:pk>/',login_required(EliminarHorario.as_view()),name = 'eliminar_horario'),
    path('eliminar_alumno/<int:pk>/',login_required(EliminarAlumno.as_view()),name = 'eliminar_alumno'),
    path('eliminar_inscripcion/<int:pk>/',login_required(EliminarInscripcion.as_view()),name = 'eliminar_inscripcion'),
    #path('eliminar_inscripcion_profesor/<int:pk>/',login_required(EliminarInscripcionProfesor.as_view()),name = 'eliminar_inscripcion_profesor'),
    path('eliminar_administrador/<int:pk>/',login_required(EliminarAdministrador.as_view()),name = 'eliminar_administrador'),
    path('eliminar_profesor/<int:pk>/',login_required(EliminarProfesor.as_view()),name = 'eliminar_profesor'),
    path('eliminar_materia/<int:pk>/',login_required(EliminarMateria.as_view()),name = 'eliminar_materia'),
    path('eliminar_notas/<int:pk>/',login_required(EliminarNotas.as_view()),name = 'eliminar_notas'),
    path('eliminar_carrera/<int:pk>/',login_required(EliminarCarrera.as_view()),name = 'eliminar_carrera'),
    path('eliminar_asistencia/<int:pk>/',login_required(EliminarAsistencia.as_view()),name = 'eliminar_asistencia'),
    path('eliminar_fecha/<int:pk>/',login_required(EliminarFecha.as_view()),name = 'eliminar_fecha'),
    path('eliminar_inscripcion_profesor/<int:pk>/',login_required(EliminarInscripcionProfesor.as_view()),name = 'eliminar_inscripcion_profesor'),
    path('eliminar_inscripcion_examen/<int:pk>/',login_required(EliminarInscripcionExamen.as_view()),name = 'eliminar_inscripcion_examen'),
    path('eliminar_inscripcion_examen_alumno/<int:pk>/',login_required(EliminarInscripcionExamenAlumno.as_view()),name = 'eliminar_inscripcion_examen_alumno'),
    
    path('detalle_carrera/<int:pk>/',login_required(DetalleCarrera.as_view()), name = 'detalle_carrera'),
    path('listar_materia_alumno/',login_required(ListadoMateriaAlumno.as_view()),name = 'listar_materia_alumno'),
    path('detalle_materia/<int:pk>/',login_required(DetalleMateria.as_view()), name = 'detalle_materia'),
    path('detalle_inscripcion/<int:pk>/',login_required(DetalleInscripcion.as_view()), name = 'detalle_inscripcion'),
    path('detalle_alumno/<int:pk>/',login_required(DetalleAlumno.as_view()), name = 'detalle_alumno'),
    path('asistencia_materia/<int:pk>/',login_required(AsistenciaMateria.as_view()), name = 'asistencia_materia'),
    path('test/',TestView.as_view(), name = 'test'),
      
]