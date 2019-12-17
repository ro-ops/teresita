from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Formulario, Usuario
from django.contrib.auth import authenticate

class PostFormulario(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ('nombre', 'correo', "telefono", "fecha", "mensaje")
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese su Nombre'}),
            'correo': forms.TextInput(attrs={'placeholder': 'ejemplo@gmail.com'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese telefono'}),
            'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Selecione su fecha de nacimiento.', 'type':'date'}),
            'mensaje': forms.Textarea(
                attrs={'placeholder': 'Deje su mensaje aquí'}),
        }
        
class RecuperarForm(forms.Form):
#     nombre = forms.CharField(required=False)
    class Meta: 
        model = Formulario
        fields = ["correo"]
    correo = forms.EmailField(required=True)
    def clean_correo(self):
        correo = self.cleaned_data.get("correo")
        return correo

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = Usuario
        fields = ("email", "username", "password1", "password2")

class AutenticacionUsuario(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email', 'password')
    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Usuario Inválido")
        