"""teresita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from botilleria import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('formularios', views.FormularioViewSet)

urlpatterns = [
    path('botilleria/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('botilleria.urls')),
    path('nosotros', views.nosotros),
    path('ofertas', views.ofertas),
    path('productos', views.productos),
    path('registrar', views.registrar),
    path('login',views.login),
    path('logout',views.logout),
    path('recuperar',views.recuperar),
]
