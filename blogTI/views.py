from rest_framework import viewsets
from .models import Usuario, Publicacion, Etiqueta, Reposteo, Comentario

from .serializers import UsuarioSerializer, PublicacionSerializer, EtiquetaSerializer, ReposteoSerializer, ComentarioSerializer, UserSerializer
from django.http import HttpResponse
from django.core.cache import cache
from django.contrib import messages

from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username='username')
    except User.DoesNotExist:
        return Response('Usuario inválido')
    
    pwd_valid = check_password(password, user.password)
    if not pwd_valid:
        return Response('contraseña inválida')
    token, created = Token.objects.get_or_create.create(user=user)
    print(token.key)
    return Response(token.key)


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

#implementación de redis
def prueba_cache(request):

    cache.set("my_key", "Hello World", 600)

    value = cache.get("my_key")

    return HttpResponse("La cache fue creada y consultada")

# prueba crud

def home(request):
    publicacionListados = Publicacion.objects.all()
    messages.success(request, '¡Publicaciones listadas!')
    return render(request, "gestionPost.html", {"Publicacion": publicacionListados})


def registrarPublicacion(request):
    user_id = request.POST['user_id']
    title = request.POST['title']
    content = request.POST['content']

    publicacion = Publicacion.objects.create(
        user_id=user_id,title=title, content=content
        #, num_reaction=num_reaction, num_repost=num_repost,num_comments=num_comments
         )
    messages.success(request, '¡Publicación registrada!')
    return redirect('/blogTI')


def edicionPublicacion(request, id):
    publicacion = Publicacion.objects.get(id=id)
    return render(request, "edicionPublicacion.html", {"Publicacion": publicacion})


def editarPublicacion(request, id):
    #user_id = request.POST['user_id']
    title = request.POST['title']
    content = request.POST['content']

    

    messages.success(request, '¡Publicación actualizada!')

    return redirect('/blogTI')


def eliminarPublicacion(request, id):
    publicacion = Publicacion.objects.get(id=id)
    publicacion.delete()

    messages.success(request, '¡Publicación eliminada!')

    return redirect('/blogTI')

