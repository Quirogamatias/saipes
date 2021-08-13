from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from .models import *

class UsuarioManager(BaseUserManager):
    def _create_user(self, username, email, nombres, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            nombres=nombres,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, nombres, is_staff, password=None, **extra_fields):
        return self._create_user(username, email, nombres, password, is_staff, False, **extra_fields)
    
    def create_superuser(self,username,email,nombres,password = None,**extra_fields):
        return self._create_user(username, email, nombres, password, True, True, **extra_fields)



class Usuario(AbstractBaseUser,PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electronico', max_length=254,unique=True)
    nombres = models.CharField('Nombres',max_length=200, blank=True,null=True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True,null=True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/',max_length=200,blank=True,null=True)
    is_active = models.BooleanField(default=True)#usuario activo
    is_staff = models.BooleanField(default=False)#usuario administrador
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres','apellidos']

    class Meta:
        permissions = [('permiso_desde_codigo','Este es un permiso creado desde codigo'),
                        ('segundo_permiso_codigo','segundo permiso creado desde codigo')]

    def __str__(self):
        #return self.nombres,self.apellidos
        return f'{self.apellidos},{self.nombres}'

