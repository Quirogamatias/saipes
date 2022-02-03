from django.contrib import admin
from .models import *

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
