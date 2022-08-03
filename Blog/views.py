from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    posts= Post.objects.filter(estado=True)
    return render (request,'index.html', {'post' : posts})

def about(request):
    return render (request, 'about.html')

def general(request):
    posts= Post.objects.filter(
        estado=True, 
        categoria = Categoria.objects.get(nombre='General')
        )
    return render (request, 'general.html',  {'post' : posts})

def programacion(request):
    posts= Post.objects.filter(
        estado=True,
        categoria = Categoria.objects.get(nombre='Programacion')
        )
    return render (request, 'programacion.html',{'post' : posts})

def libros(request):
    posts= Post.objects.filter(
        estado=True, 
        categoria = Categoria.objects.get(nombre='Libros')
        )
    return render (request, 'libros.html',{'post' : posts})

def juegos(request):
    posts= Post.objects.filter(
        estado=True, 
        categoria = Categoria.objects.get(nombre='Juegos')
        )
    return render (request, 'juegos.html', {'post' : posts})

def detallePost(request,slug):
    posts= Post.objects.get(
        slug=slug,
        
        )
    return render(request,'post.html', {'detallepost': posts})