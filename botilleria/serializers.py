from .models import Formulario
from rest_framework import serializers

class FormularioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Formulario
    # fields = ['id', 'nombre', 'correo', 'telefono', 'fecha', 'mensaje']
    fields = '__all__'