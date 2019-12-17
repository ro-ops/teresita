from .models import Formulario, Usuario
from rest_framework import serializers

class FormularioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Formulario
    # fields = ['id', 'nombre', 'correo', 'telefono', 'fecha', 'mensaje']
    fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    # fields = ['id', 'email', 'username', 'is_admin', 'fecha_registro']
    fields = '__all__'