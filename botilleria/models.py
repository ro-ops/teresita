from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    fecha = models.DateField(blank=True, null=True)
    mensaje = models.CharField(max_length=100)

    def publish(self):
        self.fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class ControlCuenta(BaseUserManager):
        def create_user(self,email,username, password=None):
                if not email:
                        raise ValueError('El usuario debe contener un correo electrónico.')
                if not username:
                        raise ValueError('El usuario debe contener un nombre de usuario.')
                
                user = self.model(
                        email=self.normalize_email(email),
                        username=username,
                )

                user.set_password(password)
                user.save(using=self.db)
                return user
        def create_superuser(self,email,username,password):
                user = self.create_user(
                        email = self.normalize_email(email),
                        password=password,
                        username=username,
                )
                user.is_admin = True
                user.is_staff = True
                user.is_superuser = True
                user.save(using=self._db)
                return user

class Usuario(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    fecha_registro = models.DateTimeField(verbose_name='fecha_registro', auto_now_add=True)
    ultimo_login = models.DateTimeField(verbose_name='ultimo_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = ControlCuenta()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


    