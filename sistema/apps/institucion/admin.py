from django.contrib import admin
from .models import *

class RespuestaInline(admin.StackedInline):
    model = Respuesta
    extra = 3

class PreguntaAdmin(admin.ModelAdmin):
    inline = [RespuestaInline]
    list_display = ('asunto', 'fecha_publicacion', 'publicado_hoy')
    #list_filter = ('fecha_publicacion')

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Administrador)
admin.site.register(Inscripcion)
admin.site.register(Carrera)
admin.site.register(Materia)
admin.site.register(Curso)
admin.site.register(Horario)
admin.site.register(Notas)
admin.site.register(Asistencia)
admin.site.register(Fecha)
admin.site.register(PromedioAsistencia)
admin.site.register(PromedioNotasFinal)
admin.site.register(PromedioNotasParcial)
admin.site.register(InscripcionProfesor)
admin.site.register(InscripcionExamen)
admin.site.register(Pregunta,PreguntaAdmin)
admin.site.register(Respuesta)
