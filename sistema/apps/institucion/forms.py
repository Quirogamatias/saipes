from django.forms import *
from django import forms
from django.db.models import fields
from .models import *
from apps.usuario.models import Usuario

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
            'turno':forms.Select(
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
        fields = ['dia','hora_inicio','hora_fin','id_curso']
        labels = {
            'dia': 'dia',
            'hora_inicio': 'hora de inico',
            'hora_fin': 'hora de fin',
            'id_curso': 'curso',

        }
        widgets = {
            'dia': forms.Select(
                attrs = {
                    'class':'form-control'
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
            'id_curso':forms.Select(
                attrs = {
                    'class':'form-control'
                }
            )
        }

class AlumnoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_carrera'].queryset = Carrera.objects.filter(estado = True)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)

    class Meta:
        model = Alumno
        fields = ['dni','nombre','apellido','email','domicilio','telefono','id_carrera','notificacion','id_usuario']
        labels = {
            'dni': 'dni del alumno',
            'nombre': 'nombre del alumno',
            'apellido': 'apellido del alumno',
            'email': 'email el alumno ',
            'domicilio': 'domicilio del alumno',
            'telefono': 'telefono del alumno',
            'id_carrera': 'carrera del Alumno',
            'notificacion': 'notificacion del Alumno',
            'id_usuario': 'id_usuario',
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
            'id_carrera':forms.SelectMultiple(
                attrs = {
                    'class':'form-control',
                }
            ),
            'notificacion':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_usuario':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
        }

class Alumno2Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_carrera'].queryset = Carrera.objects.filter(estado = True)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)

    class Meta:
        model = Alumno
        fields = ['dni','nombre','apellido','email','domicilio','telefono','id_carrera','notificacion','id_usuario']
        labels = {
            'dni': 'dni del alumno',
            'nombre': 'nombre del alumno',
            'apellido': 'apellido del alumno',
            'email': 'email el alumno ',
            'domicilio': 'domicilio del alumno',
            'telefono': 'telefono del alumno',
            'id_carrera': 'carrera del Alumno',
            'notificacion': 'notificacion del Alumno',
            'id_usuario': 'id_usuario',
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
            'id_carrera':forms.SelectMultiple(
                attrs = {
                    'class':'form-control',
                }
            ),
            'notificacion':forms.Select(
                attrs = {
                    'class':'form-control',
                    
                }
            ),
            'id_usuario':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            )
        }

class Alumno3Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['id_carrera'].queryset = Carrera.objects.filter(estado = True)
        #self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)

    class Meta:
        model = Alumno
        fields = ['dni','nombre','apellido','email','domicilio','telefono','notificacion']
        labels = {
            'dni': 'dni del alumno',
            'nombre': 'nombre del alumno',
            'apellido': 'apellido del alumno',
            'email': 'email el alumno ',
            'domicilio': 'domicilio del alumno',
            'telefono': 'telefono del alumno',
            'notificacion': 'notificacion del Alumno',
        }
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'apellido':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
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
            'notificacion':forms.Select(
                attrs = {
                    'class':'form-control',
                    
                }
            )
        }


class InscripcionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_alumno'].queryset = Alumno.objects.none()
        self.fields['id_materia'].queryset = Materia.objects.filter(estado = True)

    class Meta:
        model = Inscripcion
        fields = ['fecha_inscripcion','id_alumno','id_materia']
        labels = {
            'fecha_inscripcion': 'fecha_inscripcion',
            'id_alumno': 'id_alumno',
            'id_materia': 'id_materia',

        }
        widgets = {
            'fecha_inscripcion': forms.SelectDateWidget(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_materia':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ), 
            'id_alumno': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
                       
        }

class Inscripcion2Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_alumno'].queryset = Alumno.objects.filter(estado = True)
        self.fields['id_materia'].queryset = Materia.objects.filter(estado = True)

    class Meta:
        model = Inscripcion
        fields = ['fecha_inscripcion','id_alumno','id_materia']
        labels = {
            'fecha_inscripcion': 'fecha_inscripcion',
            'id_alumno': 'id_alumno',
            'id_materia': 'id_materia',

        }
        widgets = {
            'fecha_inscripcion': forms.SelectDateWidget(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_materia':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ), 
            'id_alumno': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )
                       
        }

class AdministradorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)


    class Meta:
        model = Administrador
        fields = ['nombre','apellido','telefono','domicilio','email','notificacion','id_usuario']
        labels = {
            'nombre': 'nombre del administrador',
            'apellido': 'apellido del administrador',
            'telefono': 'telefono del administrador',
            'domicilio': 'domicilio del administrador ',
            'email': 'email del administrador',
            'notificacion': 'notificacion del Alumno',
            'id_usuario': 'id_usuario',

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
            ),
            'notificacion':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_usuario':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )          
        }

class ProfesorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_usuario'].queryset = Usuario.objects.filter(is_active = True)


    class Meta:
        model = Profesor
        fields = ['dni','nombre','apellido','email','domicilio','telefono','notificacion','id_usuario']
        labels = {
            'dni': 'dni del profesor',
            'nombre': 'nombre del profesor',
            'apellido': 'apellido del profesor',
            'email': 'email del profesor ',
            'domicilio': 'domicilio del profesor',
            'telefono': 'telefono del profesor',
            'notificacion': 'notificacion del Alumno',
            'id_usuario': 'id_usuario',

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
            'notificacion':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_usuario':forms.Select(
                attrs = {
                    'class':'form-control',
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
            'id_horario': 'horario de la materia'

        }
        widgets = {
            'materia': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la materia'
                }
            ),
            'id_horario': forms.SelectMultiple(
                attrs = {
                    'class':'form-control'
                }
            )
        }

class Notas2Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_materia'].queryset = Materia.objects.filter(estado = True)
        self.fields['id_alumno'].queryset = Alumno.objects.filter(estado = True)
        #sku = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = Notas
        fields = ['notas','id_materia','id_alumno','tipo']

        labels = {
            'notas': 'notas',
            'id_materia': 'id de la materia',
            'id_alumno': 'id del alumno',
            'tipo': 'tipo de Examen',

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
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'id_alumno':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
                }
            ),
            'tipo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'readonly':'readonly'
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
        fields = ['notas','id_materia','id_alumno','tipo']

        labels = {
            'notas': 'notas',
            'id_materia': 'id de la materia',
            'id_alumno': 'id del alumno',
            'tipo': 'tipo de Examen',

        }
        
        widgets = {
            'notas': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese las notas'
                }
            ),
            'id_materia': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            ),
            'id_alumno':forms.Select(
                attrs = {
                    'class':'form-control'
                }
            ),
            'tipo': forms.Select(
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
            'id_materia': forms.SelectMultiple(
                attrs = {
                    'class':'form-control'
                }
            )
        }
        
class AsistenciaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_materia'].queryset = Materia.objects.filter(estado = True)
        self.fields['id_alumno'].queryset = Alumno.objects.filter(estado = True)

    class Meta:
        model = Asistencia
        fields = ['id_materia','id_alumno','dia','asistencia']
        labels = {
            'id_materia': 'id_materia',
            'id_alumno': 'id_alumno',
            'dia': 'dia',
            'asistencia': 'asistencia',

        }
        widgets = {
            'id_materia': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_alumno': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            ),
            'dia': forms.SelectDateWidget(
                attrs = {
                    'class':'form-control',
                }
            ),
            'asistencia':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )            
        }

class FechaForm(forms.ModelForm):

    class Meta:
        model = Fecha
        fields = ['fecha_evento','evento']
        labels = {
            'fecha_evento': 'fecha de evento',
            'evento': 'nombre del evento'

        }
        widgets = {
            'fecha_evento': forms.SelectDateWidget(
                attrs = {
                    'class':'form-control',
                }
            ),
            'evento': forms.TextInput(
                attrs = {
                    'class':'form-control',                    
                    'placeholder':'Ingrese el evento de la Fecha'
                }
            )
        }

class PromedioAsistenciaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_materia'].queryset = Materia.objects.filter(estado = True)
        self.fields['id_alumno'].queryset = Alumno.objects.filter(estado = True)
        
    class Meta:
        model = PromedioAsistencia
        fields = ['id_materia','id_alumno']
        labels = {
            'id_materia': 'id_materia',
            'id_alumno': 'id_alumno',

        }
        widgets = {
            'id_materia': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_alumno': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            )          
        }

class PromedioNotasFinalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_materia'].queryset = Materia.objects.filter(estado = True)
        self.fields['id_alumno'].queryset = Alumno.objects.filter(estado = True)
        
    class Meta:
        model = PromedioNotasFinal
        fields = ['id_materia','id_alumno']
        labels = {
            'id_materia': 'id_materia',
            'id_alumno': 'id_alumno',

        }
        widgets = {
            'id_materia': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_alumno': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            )          
        }

class PromedioNotasParcialForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_materia'].queryset = Materia.objects.filter(estado = True)
        self.fields['id_alumno'].queryset = Alumno.objects.filter(estado = True)
        
    class Meta:
        model = PromedioNotasParcial
        fields = ['id_materia','id_alumno']
        labels = {
            'id_materia': 'id_materia',
            'id_alumno': 'id_alumno',

        }
        widgets = {
            'id_materia': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_alumno': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            )          
        }

class InscripcionProfesorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_profesor'].queryset = Profesor.objects.filter(estado = True)
        self.fields['id_materia'].queryset = Materia.objects.filter(estado = True)

    class Meta:
        model = InscripcionProfesor
        fields = ['fecha_inscripcion','id_profesor','id_materia']
        labels = {
            'fecha_inscripcion': 'fecha_inscripcion',
            'id_profesor': 'id_profesor',
            'id_materia': 'id_materia',

        }
        widgets = {
            'fecha_inscripcion': forms.SelectDateWidget(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_profesor': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_materia':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )            
        }

class InscripcionExamenForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_alumno'].queryset = Alumno.objects.filter(estado = True)
        self.fields['id_materia'].queryset = Materia.objects.filter(estado = True)

    class Meta:
        model = InscripcionExamen
        fields = ['fecha','id_alumno','id_materia']
        labels = {
            'fecha': 'fecha',
            'id_alumno': 'id_alumno',
            'id_materia': 'id_materia',

        }
        widgets = {
            'fecha': forms.SelectDateWidget(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la fecha de inscripcion'
                }
            ),
            'id_alumno': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'id_materia':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            )            
        }

class TestForm(Form):
    carrera = ModelChoiceField(queryset=Carrera.objects.all(),widget=Select(attrs={
        'class': 'form-control'
    }))

    materia = forms.ModelChoiceField(queryset=Materia.objects.none(),widget=forms.Select(attrs={
        'class': 'form-control'
    }))

class ListForm(Form):
    materia = forms.ModelChoiceField(queryset=Materia.objects.all(),widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    alumno = ModelChoiceField(queryset=Alumno.objects.none(),widget=Select(attrs={
        'class': 'form-control'
    }))

    #alumno = forms.ModelChoiceField(queryset=Inscripcion.objects.none(),widget=forms.Select(attrs={
     #   'class': 'form-control'
    #}))
