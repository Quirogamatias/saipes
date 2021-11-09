from django.db import models
from django.utils import timezone
from apps.usuario.models import Usuario
from django.db.models.signals import post_save


class Curso(models.Model):
    id_curso = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre del curso',max_length=100, null=False, blank = False)
    capacidad = models.CharField('capacidad del curso',max_length=100, null=False, blank = False)
    t = (
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    )
    turno = models.CharField('turno del curso',max_length=100,choices=t, null=False, blank = False)
    estado = models.BooleanField('Curso activado/no activado', default= True)

    def natural_key(self):
        return f'Nombre del Curso: {self.nombre}, Capacidad: {self.capacidad}, Turno: {self.turno}'
       
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nombre']

    def __str__(self):
        return f'Nombre del Curso: {self.nombre},Capacidad: {self.capacidad}, Turno: {self.turno}'
      
class Horario(models.Model):
    id_horario = models.AutoField(primary_key= True)
    dias = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sabado'),
    )
    dia = models.CharField('Dia',max_length=100,choices=dias, null=False, blank = False)
    hora_inicio = models.CharField('Hora de inicio',max_length=100, null=False, blank = False)
    hora_fin = models.CharField('Hora de fin',max_length=100, null=False, blank = False)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)#un horario puede tener varios curso
    estado = models.BooleanField('Horario activado/no activado', default= True)

    def natural_key(self):
        return f'Dia {self.dia}, horario inicio {self.hora_inicio}, horario final {self.hora_fin}, Curso {self.id_curso}'    
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['dia']

    def __str__(self):
        return f'Dia {self.dia}, Hora de Inicio {self.hora_inicio}, Hora de Fin{self.hora_fin}, Curso {self.id_curso}'

def quitar_relacion_curso_horario(sender,instance,**kwargs):
    if instance.estado == False:
        curso = instance.id_curso
        horario = Horario.objects.filter(id_curso=curso)
        for horario in horario:
            horario.id_curso.remove(curso)

class Materia(models.Model):
    id_materia = models.AutoField(primary_key= True)
    materia = models.CharField('Materia',max_length=100, null=False, blank = False)
    estado = models.BooleanField('Materia activado/no activado', default= True)
    id_horario = models.ManyToManyField(Horario)

    def natural_key(self):
        return self.materia
    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['materia']

    def __str__(self):
        return self.materia

    def obtener_horarios(self):
        horarios = str([horario for horario in self.id_horario.all().values_list('dia','hora_inicio','hora_fin')]).replace("[","").replace("]","").replace("'","")
        return horarios
    
    def obtener_horario(self):
        horarios = str([horario for horario in self.id_horario.all()])
        return horarios
    
 
#def quitar_relacion_horario_materia(sender,instance,**kwargs):
 #   if instance.estado == False:
  #      horario = instance.id_horario
   #     materia = Materia.objects.filter(id_horario=horario)
    #    for materia in materia:
     #       materia.horario.remove(horario)

class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key= True)
    carrera = models.CharField('Carrera',max_length=100, null=False, blank = False)
    id_materia = models.ManyToManyField(Materia)
    #duracion
    estado = models.BooleanField('Carrera activado/no activado', default= True)
    
    def natural_key(self):
        return self.carrera
    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        ordering = ['carrera']

    def __str__(self):
        return self.carrera
    
    def obtener_materias(self):
        materias = str([materia for materia in self.id_materia.all().values_list('materia',flat = True)]).replace("[","").replace("]","").replace("'","")
        return materias
    
    def obtener_materia(self):
        materias = str([materia for materia in self.id_materia.all().values_list('materia',flat = True)]).replace("[","").replace("]","").replace("'","")      
        #a= len(materias) el len es para saver la cantidad de elementos que tienen la lista en este caso 35
        
        return materias

def quitar_relacion_materia_carrera(sender,instance,**kwargs):
    if instance.estado == False:
        materia = instance.id_materia
        carrera = Carrera.objects.filter(id_materia=materia)
        for carrera in carrera:
            carrera.materia.remove(materia)

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
    id_usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, null=True, blank = True)
    t = (
        (True,'activo'),
        (False,'desactivado'),
    )
    notificacion = models.BooleanField('notificacion activado/no activado',choices=t, default= True,null=True, blank = True)
    id_carrera = models.ManyToManyField(Carrera)
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def natural_key(self):
        #return self.apellido
        return f'Apellido {self.apellido}, Nombre {self.nombre}'
    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['apellido']

    def __str__(self):
        return f'Alumno {self.apellido}, Nombre {self.nombre}'

def quitar_relacion_carrera_alumno(sender,instance,**kwargs):
    if instance.estado == False:
        carrera = instance.id_carrera
        alumno = Alumno.objects.filter(id_carrera=carrera)
        for alumno in alumno:
            alumno.carrera.remove(carrera)


class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key= True)
    fecha_inscripcion = models.DateTimeField('Fecha de creacion', default=timezone.now)
    id_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    estado = models.BooleanField('Inscripcion activado/no activado', default= True)

    def natural_key(self):
        return f'Materia {self.materia}, Alumno {self.apellido}, Fecha inscripcion {self.fecha_inscripcion}'
   
    class Meta:
        verbose_name = 'Inscripcion'
        verbose_name_plural = 'Inscripciones'
        ordering = ['id_inscripcion']
    def __str__(self):
        return f'Materia {self.id_materia}, Alumno {self.id_alumno}, Fechainscripcion {self.fecha_inscripcion}'
   
    
    def obtener_alumnos(self):
        alumnos = str([Alumno for Alumno in self.id_alumno.all().values_list('apellido',flat = True)]).replace("[","").replace("]","").replace("'","")
        return alumnos
    
    def obtener_materia(self):
        materias = str([Materia for Materia in self.id_materia.all().values_list('materia',flat = True)]).replace("[","").replace("]","").replace("'","")
        return materias

def quitar_relacion_alumno_materia_inscripcion(sender,instance,**kwargs):
    if instance.estado == False:
        alumno = instance.id_alumno
        inscripcion = Inscripcion.objects.filter(id_alumno=alumno)
        for inscripcion in inscripcion:
            inscripcion.id_alumno.remove(alumno)
        materia = instance.id_materia
        inscripcion2 = Inscripcion.objects.filter(id_materia=materia)
        for inscripcion2 in inscripcion:
            inscripcion2.id_materia.remove(materia)

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
    id_usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, null=True, blank = True)
    t = (
        (True,'activo'),
        (False,'desactivado'),
    )
    notificacion = models.BooleanField('notificacion activado/no activado',choices=t, default= True,null=True, blank = True)

    def natural_key(self):
        return f'Administrador {self.apellido}, Nombre {self.nombre}'

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        ordering = ['apellido']

    def __str__(self):
        return f'Administrador {self.apellido}, Nombre {self.nombre}'

class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key= True)
    dni = models.CharField('Dni',max_length=100, null=False, blank = False)
    nombre = models.CharField('Nombre del profesor',max_length=100, null=False, blank = False)
    apellido = models.CharField('Apellido del profesor',max_length=100, null=False, blank = False)
    email = models.EmailField('Correo Electronico', blank=False,null=False)
    domicilio = models.CharField('domicilio del profesor',max_length=100, null=False, blank = False)
    telefono = models.CharField('telefono del profesor',max_length=100, null=False, blank = False) 
    notificacion = models.BooleanField('notificacion activado/no activado', default= True)
    estado = models.BooleanField('Profesor activado/no activado', default= True)
    fecha_de_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    id_usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, null=True, blank = True)
    t = (
        (True,'activo'),
        (False,'desactivado'),
    )
    notificacion = models.BooleanField('notificacion activado/no activado',choices=t, default= True,null=True, blank = True)
    #id_materia = models.ManyToManyField(Materia)
    
    def natural_key(self):
        return f'Profesor {self.apellido}, Nombre {self.nombre}'
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['apellido']

    def __str__(self):
        return f'Profesor {self.apellido}, Nombre {self.nombre}'

class Notas(models.Model):
    id_notas = models.AutoField(primary_key= True)
    notas = models.FloatField('Notas',max_length=10, null=False, blank = False)
    id_materia =  models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_alumno =  models.ForeignKey(Alumno, on_delete=models.CASCADE)
    tip = (
        ('Parcial', 'Parcial'),
        ('Final', 'Final'),
    )
    tipo = models.CharField('Tipo',max_length=100,choices=tip, null=False, blank = False)    
    estado = models.BooleanField('Notas activado/no activado', default= True)
    #cantidad de finales que tiene la materia, en este caso 4
    #a=np.array([1,3,5]) b=np.array([[1,3,5],[1,3,5],[1,3,5]])
    #podria hacer que cuando creeo una nota, pregunte si esa nota existe y si existe que cree la nueva nota,si son mas de 4 notas que no cree otra nota
    def natural_key(self):
        return f'Materia {self.materia}, Alumno {self.apellido}, Promedio {self.notas}'
    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['notas']

    def __str__(self):
        return f'Materia {self.id_materia}, Alumno {self.id_alumno}, Notas {self.notas}'

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


class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key= True)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)   
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    dia = models.DateField('dia', auto_now=False, auto_now_add=False, null=False, blank = False)
    a_p = (
        ('Ausente', 'Ausente'),
        ('Presente', 'Presente'),
    )
    asistencia = models.CharField('Asistencia',max_length=100, choices=a_p, null=False, blank = False)
    #promedio= models.FloatField('Promedio',max_length=200, null=False, blank = False)
    estado = models.BooleanField('Horario activado/no activado', default= True)
    
    def natural_key(self):
        return f'Materia {self.materia}, Alumno {self.apellido}, Horario {self.dia}'
    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        ordering = ['id_asistencia']

    def __str__(self):
        return f'Materia {self.id_materia}, Alumno {self.id_alumno}, Asistencia {self.asistencia}, Dia {self.dia}'

class Fecha(models.Model):
    id_fecha = models.AutoField(primary_key= True)
    fecha_evento = models.DateField('Fecha',auto_now=False,auto_now_add=False, null=False, blank = False)
    evento= models.CharField('Evento',max_length=200, null=False, blank = False)
    estado = models.BooleanField('activado/no activado', default= True)
    fecha_de_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    def natural_key(self):
        return f'Fecha {self.fecha_evento}, Evento {self.evento}'
    class Meta:
        verbose_name = 'Fecha'
        verbose_name_plural = 'Fechas'
        ordering = ['fecha_evento']

    def __str__(self):
        return f'Fecha {self.fecha_evento}, Evento {self.evento}'

class PromedioAsistencia(models.Model):
    id_promedioasistencia = models.AutoField(primary_key= True)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)   
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    promedio= models.FloatField('Promedio',max_length=100, null=False, blank = False,default=100)
    dias = models.IntegerField('Dias',null=False, blank = False,default=0)
    dias_p = models.IntegerField('Dias Presente',null=False, blank = False,default=0)
    total_d = models.FloatField('total Dias',null=False, blank = False,default=0)
    estado = models.BooleanField('Promedio activado/no activado', default= True)
    
    def natural_key(self):
        return f'Materia {self.materia}, Alumno {self.apellido}, Promedio {self.promedio}'
   
    class Meta:
        verbose_name = 'PromedioAsistencia'
        verbose_name_plural = 'PromedioAsistencias'
        ordering = ['id_promedioasistencia']

    def __str__(self):
        return f'Materia {self.id_materia}, Alumno {self.id_alumno}, Promedio {self.promedio}'

class PromedioNotasFinal(models.Model):
    id_promedionotasfinal = models.AutoField(primary_key= True)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)   
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    cantidad = models.IntegerField('Cantidad de notas',null=False, blank = False,default=0)
    suma = models.FloatField('Suma de notas',null=False, blank = False,default=0)
    total = models.FloatField('Total de notas',null=False, blank = False,default=0)
    estado = models.BooleanField('Promedio activado/no activado', default= True)
    
    def natural_key(self):
        return f'Materia {self.materia}, Alumno {self.apellido}, Promedio {self.total}'
   
    class Meta:
        verbose_name = 'PromedioNotasFinal'
        verbose_name_plural = 'PromedioNotasFinales'
        ordering = ['id_promedionotasfinal']

    def __str__(self):
        return f'Materia {self.id_materia}, Alumno {self.id_alumno}, Promedio {self.total}'
        #3+5+6=14 14/3

class PromedioNotasParcial(models.Model):
    id_promedionotasparcial = models.AutoField(primary_key= True)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)   
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    cantidad = models.IntegerField('Cantidad de notas',null=False, blank = False,default=0)
    suma = models.FloatField('Suma de notas',null=False, blank = False,default=0)
    total = models.FloatField('Total de notas',null=False, blank = False,default=0)
    estado = models.BooleanField('Promedio activado/no activado', default= True)
    
    def natural_key(self):
        return f'Materia {self.materia}, Alumno {self.apellido}, Promedio {self.total}'
   
    class Meta:
        verbose_name = 'PromedioNotasParcial'
        verbose_name_plural = 'PromedioNotasParciales'
        ordering = ['id_promedionotasparcial']

    def __str__(self):
        return f'Materia {self.id_materia}, Alumno {self.id_alumno}, Promedio {self.total}'
 
class InscripcionExamen(models.Model):
    id_inscripcionexamen = models.AutoField(primary_key= True)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)     
    fecha = models.DateField('Fecha de creacion', default=timezone.now)
    estado = models.BooleanField('inscripcionExamen activado/no activado', default= True)
    
    def natural_key(self):
        return f'materia {self.materia}, Alumno {self.apellido}, fecha de inscripcion {self.fecha}'
   
    class Meta:
        verbose_name = 'InscripcionExamen'
        verbose_name_plural = 'InscripcionExamenes'
        ordering = ['id_inscripcionexamen']

    def __str__(self):
        return f'Materia {self.id_materia}, Alumno {self.id_alumno}, fecha de inscripcion {self.fecha}'

class InscripcionProfesor(models.Model):
    id_inscripcionProfesor = models.AutoField(primary_key= True)
    fecha_inscripcion = models.DateTimeField('Fecha de creacion', default=timezone.now)
    id_profesor = models.ForeignKey(Profesor, on_delete = models.CASCADE)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    estado = models.BooleanField('Inscripcion activado/no activado', default= True)

    def natural_key(self):
        return f'Materia {self.materia}, Profesor {self.apellido}'
   
    class Meta:
        verbose_name = 'InscripcionProfesor'
        verbose_name_plural = 'InscripcionProfesores'
        ordering = ['id_inscripcionProfesor']
    def __str__(self):
        return f'Materia {self.id_materia}, Profesor {self.id_profesor}'
   
    
    def obtener_profesor(self):
        profesores = str([Profesor for Profesor in self.id_profesor.all().values_list('apellido',flat = True)]).replace("[","").replace("]","").replace("'","")
        return profesores
    
    def obtener_materia(self):
        materias = str([Materia for Materia in self.id_materia.all().values_list('materia',flat = True)]).replace("[","").replace("]","").replace("'","")
        return materias
