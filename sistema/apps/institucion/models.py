from django.db import models
from django.utils import timezone


class Curso(models.Model):
    id_curso = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre del curso',max_length=100, null=False, blank = False)
    capacidad = models.CharField('capacidad del curso',max_length=100, null=False, blank = False)
    turno = models.CharField('turno del curso',max_length=100, null=False, blank = False)
    estado = models.BooleanField('Curso activado/no activado', default= True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    id_horario = models.AutoField(primary_key= True)
    dia = models.DateTimeField('Dia', default=timezone.now)
    hora_inicio = models.CharField('Hora de inicio',max_length=100, null=False, blank = False)
    hora_fin = models.CharField('Hora de fin',max_length=100, null=False, blank = False)
    asistencia = models.CharField('Asistencia',max_length=100, null=False, blank = False)
    id_curso = models.OneToOneField(Curso, on_delete = models.CASCADE)
    estado = models.BooleanField('Horario activado/no activado', default= True)
    
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['dia']

    def __str__(self):
        return str(self.dia)

def quitar_relacion_curso_horario(sender,instance,**kwargs):
    if instance.estado == False:
        curso = instance.id_curso
        horario = Horario.objects.filter(id_curso=curso)
        for horario in horario:
            horario.id_curso.remove(curso)

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key= True)
    dni = models.CharField('DNI del alumno',max_length=100, null=False, blank = False)
    nombre = models.CharField('Nombre del Alumno',max_length=100, null=False, blank = False)
    apellido = models.CharField('Apellido del alumno',max_length=100, null=False, blank = False)
    email = models.EmailField('Correo Electronico', blank=False,null=False)
    domicilio = models.CharField('domicilio del alumno',max_length=100, null=False, blank = False)
    telefono = models.CharField('telefono del alumno',max_length=100, null=False, blank = False)
    estado = models.BooleanField('Alumno activado/no activado', default= True)
    fecha_de_creacion = models.DateField('Fecha de creacion', auto_now=True, auto_now_add=False)
    #id_usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE)
    id_horario = models.ForeignKey(Horario, on_delete = models.CASCADE)

    def natural_key(self):
        return self.apellido

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['apellido']

    def __str__(self):
        return self.apellido

def quitar_relacion_horario_alumno(sender,instance,**kwargs):
    if instance.estado == False:
        horario = instance.id_horario
        alumno = Alumno.objects.filter(id_horario=horario)
        for alumno in alumno:
            alumno.horario.remove(horario)


class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key= True)
    fecha_inscripcion = models.DateTimeField('Fecha de creacion', default=timezone.now)
    id_alumno = models.OneToOneField(Alumno, on_delete = models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    estado = models.BooleanField('Inscripcion activado/no activado', default= True)

    class Meta:
        verbose_name = 'Inscripcion'
        verbose_name_plural = 'Inscripciones'
        ordering = ['id_inscripcion']

    def __str__(self):
        return str(self.id_inscripcion)
    
    
    def obtener_alumnos(self):
        alumnos = str([Alumno for Alumno in self.id_alumno.all().values_list('apellido',flat = True)]).replace("[","").replace("]","").replace("'","")
        return alumnos
    
    def obtener_cursos(self):
        cursos = str([Curso for Curso in self.id_curso.all().values_list('nombre',flat = True)]).replace("[","").replace("]","").replace("'","")
        return cursos

def quitar_relacion_alumno_curso_inscripcion(sender,instance,**kwargs):
    if instance.estado == False:
        alumno = instance.id_alumno
        inscripcion = Inscripcion.objects.filter(id_alumno=alumno)
        for inscripcion in inscripcion:
            inscripcion.id_alumno.remove(alumno)
        curso = instance.id_curso
        inscripcion2 = Inscripcion.objects.filter(id_curso=curso)
        for inscripcion2 in inscripcion:
            inscripcion2.id_curso.remove(curso)

class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre del Administrador',max_length=100, null=False, blank = False)
    apellido = models.CharField('Apellido del Administrador',max_length=100, null=False, blank = False)
    telefono =models.CharField('Telefono del Administrador',max_length=100, null=False, blank = False)
    domicilio = models.CharField('Domicilio del Administrador',max_length=100, null=False, blank = False)
    email = models.EmailField('Correo Electronico', blank=False,null=False)
    #id_usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE)
    estado = models.BooleanField('Administrador activado/no activado', default= True)
    fecha_de_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        ordering = ['apellido']

    def __str__(self):
        return str(self.apellido)

class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key= True)
    dni = models.CharField('Dni',max_length=100, null=False, blank = False)
    nombre = models.CharField('Nombre del profesor',max_length=100, null=False, blank = False)
    apellido = models.CharField('Apellido del profesor',max_length=100, null=False, blank = False)
    email = models.EmailField('Correo Electronico', blank=False,null=False)
    domicilio = models.CharField('domicilio del profesor',max_length=100, null=False, blank = False)
    telefono = models.CharField('telefono del profesor',max_length=100, null=False, blank = False) 
    #id_usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE)
    estado = models.BooleanField('Profesor activado/no activado', default= True)
    fecha_de_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    id_horario = models.ForeignKey(Horario, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['apellido']

    def __str__(self):
        return self.apellido

def quitar_relacion_horario_profesor(sender,instance,**kwargs):
    if instance.estado == False:
        horario = instance.id_horario
        profesor = Profesor.objects.filter(id_horario=horario)
        for profesor in profesor:
            profesor.horario.remove(horario)


class Materia(models.Model):
    id_materia = models.AutoField(primary_key= True)
    materia = models.CharField('Materia',max_length=100, null=False, blank = False)
    estado = models.BooleanField('Materia activado/no activado', default= True)
    id_horario = models.ForeignKey(Horario, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['materia']

    def __str__(self):
        return self.materia

def quitar_relacion_horario_materia(sender,instance,**kwargs):
    if instance.estado == False:
        horario = instance.id_horario
        materia = Materia.objects.filter(id_horario=horario)
        for materia in materia:
            materia.horario.remove(horario)

class Notas(models.Model):
    id_notas = models.AutoField(primary_key= True)
    notas = models.CharField('Notas',max_length=100, null=False, blank = False)
    id_materia =  models.OneToOneField(Materia, on_delete = models.CASCADE)
    id_alumno =  models.OneToOneField(Alumno, on_delete = models.CASCADE)
    estado = models.BooleanField('Notas activado/no activado', default= True)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['notas']

    def __str__(self):
        return self.notas

def quitar_relacion_materia_alumno_notas(sender,instance,**kwargs):
    if instance.estado == False:        
        materia = instance.id_materia
        notas = Notas.objects.filter(id_materia=materia)
        for notas in notas:
            notas.id_materia.remove(materia)
        alumno = instance.id_alumno
        notas2 = Notas.objects.filter(id_alumno=alumno)
        for notas2 in notas2:
            notas2.id_alumno.remove(alumno)

class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key= True)
    carrera = models.CharField('Carrera',max_length=100, null=False, blank = False)
    id_materia = models.ForeignKey(Materia, on_delete = models.CASCADE)
    estado = models.BooleanField('Carrera activado/no activado', default= True)
    
    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        ordering = ['carrera']

    def __str__(self):
        return self.carrera

def quitar_relacion_materia_carrera(sender,instance,**kwargs):
    if instance.estado == False:
        materia = instance.id_materia
        carrera = Carrera.objects.filter(id_materia=materia)
        for carrera in carrera:
            carrera.materia.remove(materia)