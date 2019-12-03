from django.db import models
from django.utils import timezone

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

