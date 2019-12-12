from django.shortcuts import render, redirect
from django.utils.timezone import timezone
from .forms import PostFormulario, RecuperarForm

from django.conf import settings
from django.core.mail import send_mail

from .models import Formulario
from .serializers import FormularioSerializer
from rest_framework import viewsets

from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class FormularioViewSet(viewsets.ModelViewSet):
  queryset = Formulario.objects.all()
  serializer_class = FormularioSerializer


def index(request):
    return render(request, 'botilleria/index.html', {})
def nosotros(request):
    if request.method == "POST":
        form = PostFormulario(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
    else:
        form = PostFormulario()
    return render(request, 'botilleria/nosotros.html', {'form': form})

def ofertas(request):
    return render(request, 'botilleria/ofertas.html')
def productos(request):
    return render(request, 'botilleria/productos.html')

#Para el registro
def registrar(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            Usuario = form.save()
            # Si el usuario se crea correctamente 
            if Usuario is not None:
                # Hacemos el login manualmente
                do_login(request, Usuario)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    # Si llegamos al final renderizamos el formulario
    return render(request, "botilleria/registrar.html", {'form': form})

#Para el login


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "botilleria/login.html", {'form': form})

#Para recuperar Contraseña
def recuperar(request):
    form = RecuperarForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # correo = form.cleaned_data['correo']
        recup_correo = form.cleaned_data.get("correo")
        # recup_link = print("")
        #recup_nombre = form.cleaned_data.get("nombre")
        asunto = 'Recuperar Contraseña'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, recup_correo]
        email_mensaje = "Hola %s . Ingrese en el siguiente link para recuperar su contraseña: " %(recup_correo)     
        
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False
            )
        return redirect('/') # Redirigir hacía página de "Se ha enviado un correo con un enlace para cambio de pass" 
    # Si llegamos al final renderizamos el formulario
    return render(request, "blog/recuperar.html", {'form': form}) 
