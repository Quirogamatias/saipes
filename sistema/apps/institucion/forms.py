from django import forms
from django.db.models import fields
from .models import *

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre','capacidad','turno']
        labels = {
            'nombre': 'Nombre del curso',
            'capacidad': 'Capacidad de curso',
            'turno': 'Turno del curso',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del curso'
                }
            ),
            'capacidad': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la capacidad del curso'
                }
            ),
            'turno':forms.TextInput(
                attrs = {
                    'class':'form-control',
                }
            )
        }

class HorarioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_curso'].queryset = Curso.objects.filter(estado = True)

    class Meta:
        model = Horario
        fields = ['dia','hora_inicio','hora_fin','asistencia','id_curso']
        labels = {
            'dia': 'dia',
            'hora_inicio': 'hora de inico',
            'hora_fin': 'hora de fin',
            'asistencia': 'asistencia ',
            'id_curso': 'id del curso',

        }
        widgets = {
            'dia': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el dia del horario'
                }
            ),
            'hora_inicio': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la hora de inicio'
                }
            ),
            'hora_fin':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el horario de finalizacion'
                }
            ),
            'asistencia':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la asistencia'
                }
            ),
            'id_curso':forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            )
        }

class AlumnoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_horario'].queryset = Horario.objects.filter(estado = True)

    class Meta:
        model = Alumno
        fields = ['dni','nombre','apellido','email','domicilio','telefono','id_horario']
        labels = {
            'dni': 'dni del alumno',
            'nombre': 'nombre del alumno',
            'apellido': 'apellido del alumno',
            'email': 'email el alumno ',
            'domicilio': 'domicilio del alumno',
            'telefono': 'telefono del alumno',
            'id_horario': 'horario del Alumno',
            'id_usuario': 'usuario del Alumno',

        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el dni del alumno'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del alumno'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del alumno'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del alumno'
                }
            ),
            'domicilio':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el domicilio del alumno'
                }
            ),
            
            'telefono':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono del alumno'
                }
            ),
            'id_horario':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el id_horario del alumno'
                }
            )
        }

class InscripcionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_alumno'].queryset = Alumno.objects.filter(estado = True)
        self.fields['id_curso'].queryset = Curso.objects.filter(estado = True)

    class Meta:
        model = Inscripcion
        fields = ['fecha_inscripcion','id_alumno','id_curso']
        labels = {
            'fecha_inscripcion': 'fecha_inscripcion',
            'id_alumno': 'id_alumno',
            'id_curso': 'id_curso',

        }
        widgets = {
            'fecha_inscripcion': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la fecha de inscripcion'
                }
            ),
            'id_alumno': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'id_curso':forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            )            
        }

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre','apellido','telefono','domicilio','email']
        labels = {
            'nombre': 'nombre del administrador',
            'apellido': 'apellido del administrador',
            'telefono': 'telefono del administrador',
            'domicilio': 'domicilio del administrador ',
            'email': 'email del administrador',

        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del administrador'
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del administrador'
                }
            ),
            'telefono':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono del administrador'
                }
            ),
            'domicilio':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el domicilio del administrador'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del administrador'
                }
            )
        }


class ProfesorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_horario'].queryset = Horario.objects.filter(estado = True)

    class Meta:
        model = Profesor
        fields = ['dni','nombre','apellido','email','domicilio','telefono','id_horario']
        labels = {
            'dni': 'dni del profesor',
            'nombre': 'nombre del profesor',
            'apellido': 'apellido del profesor',
            'email': 'email del profesor ',
            'domicilio': 'domicilio del profesor',
            'telefono': 'telefono del profesor',
            'id_horario': 'id de horario del profesor',

        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el dni del profesor'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del profesor'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el apellido del profesor'
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el email del profesor'
                }
            ),
            'domicilio':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el domicilio del profesor'
                }
            ),
            'telefono':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el telefono del profesor'
                }
            ),
            'id_horario':forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            )
        }

class MateriaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_horario'].queryset = Horario.objects.filter(estado = True)

    class Meta:
        model = Materia
        fields = ['materia','id_horario']
        labels = {
            'materia': 'materia',
            'id_horario': 'id_horario de la materia',

        }
        widgets = {
            'materia': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la materia'
                }
            ),
            'id_horario': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            )
        }


class NotasForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_materia'].queryset = Materia.objects.filter(estado = True)
        self.fields['id_alumno'].queryset = Alumno.objects.filter(estado = True)

    class Meta:
        model = Notas
        fields = ['notas','id_materia','id_alumno']

        labels = {
            'notas': 'notas',
            'id_materia': 'id de la materia',
            'id_alumno': 'id del alumno',

        }
        widgets = {
            'notas': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese las notas'
                }
            ),
            'id_materia': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'id_alumno':forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            )
        }


class CarreraForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_materia'].queryset = Materia.objects.filter(estado = True)

    class Meta:
        model = Carrera
        fields = ['carrera','id_materia']
        labels = {
            'carrera': 'carrera',
            'id_materia': 'id de la materia de la carrera',

        }
        widgets = {
            'carrera': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la carrera'
                }
            ),
            'id_materia': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            )
        }
        