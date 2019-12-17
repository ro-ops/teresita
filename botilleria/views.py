from django.shortcuts import render, redirect
from django.utils.timezone import timezone
from .forms import PostFormulario, RecuperarForm, RegistrationForm, AutenticacionUsuario

from django.conf import settings
from django.core.mail import send_mail

from .models import Formulario, Usuario
from .serializers import FormularioSerializer, UsuarioSerializer
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

class UsuarioViewSet(viewsets.ModelViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

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

def registrar(request):
    context={}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            do_login(request, account)
            return redirect('/')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
    return render(request, "botilleria/registrar.html", context)

#Para el login

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def login(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('/')
    
    if request.POST:
        form = AutenticacionUsuario(request.POST)
        if form.is_valid():
            email= request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                do_login(request, user)
                return redirect('/')
    else:
        form = AutenticacionUsuario()
    context['login_form'] = form
    return render(request, 'botilleria/login.html',context)