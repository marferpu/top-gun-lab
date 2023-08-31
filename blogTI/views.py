from rest_framework import viewsets
from .models import Usuario, Publicacion, Etiqueta, Reposteo, Comentario
from .serializers import UsuarioSerializer, PublicacionSerializer, EtiquetaSerializer, ReposteoSerializer, ComentarioSerializer
from django.shortcuts import render
from django.http import HttpResponse

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def user_list(request):
    users = Usuario.objects.all()
    return render(request, 'blog/user_list.html', {'users': users})

class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

def post_list(request):
    posts = Publicacion.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

class ReposteoViewSet(viewsets.ModelViewSet):
    queryset = Reposteo.objects.all()
    serializer_class = ReposteoSerializer

def repost_list(request):
    reposts = Reposteo.objects.all()
    return render(request, 'blog/repost_list.html', {'reposts': reposts})

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

def comment_list(request):
    comments = Comentario.objects.all()
    return render(request, 'blog/comment_list.html', {'comments': comments})

class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

def tag_list(request):
    tags = Etiqueta.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})
