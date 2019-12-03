from django.shortcuts import render
from django.utils.timezone import timezone
from .forms import PostFormulario

from .models import Formulario
from .serializers import FormularioSerializer
from rest_framework import viewsets


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


