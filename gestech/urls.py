"""
URL configuration for gestech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from technoss.views import saludo
from django.conf import settings
from django.conf.urls.static import static
from technoss.views import novedades, listag,ofertas, acerc,buscarj



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludo, name='index'),# index anteriormente
    path('nov/', novedades, name='noved'),
    path('lisg/', listag, name='listagam'),
    path('ofer/', ofertas, name='ofer'),
    path('acercade/', acerc, name='acerca'),
    path('buscar/', buscarj, name='busqueda'),


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
