from django.shortcuts import render
from .models import Game
from django.db.models import Q
# Create your views hered.
def saludo(request):
    games=Game.objects.filter(id__in=[1,2, 3])
    return render (request,'index.html',{'games': games} )


def novedades(request):
    games = Game.objects.filter(novedades__isnull=False).exclude(novedades__exact='')
    return render(request, 'noved.html', {'games': games})

def listag(request):
    games=Game.objects.all()
    return render (request,'listagam.html',{'games': games} )

def ofertas(request):
    games = Game.objects.filter(oferta__isnull=False).exclude(oferta__exact='')
    return render(request, 'ofer.html', {'games': games})

def acerc(request):
    games=Game.objects.all()
    return render (request,'acerca.html',{'games': games} )

def buscarj(request):
    query = request.GET.get('q')
    games = []
    if query:
        games = Game.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(genre__icontains=query)
        )
    return render(request, 'busqueda.html', {'resultados': games, 'query': query})