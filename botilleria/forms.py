from django import forms
from .models import Formulario

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