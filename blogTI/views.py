from rest_framework import viewsets
from .models import Publicacion, Etiqueta, Reposteo, Comentario
from .serializers import PublicacionSerializer, EtiquetaSerializer, ReposteoSerializer, ComentarioSerializer, UserSerializer
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
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('Usuario inválido')
    
    pwd_valid = check_password(password, user.password)
    if not pwd_valid:
        return Response('contraseña inválida')
    token, created = Token.objects.get_or_create(user=user)
    print(token.key)
    return Response(token.key)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class ReposteoViewSet(viewsets.ModelViewSet):
    queryset = Reposteo.objects.all()
    serializer_class = ReposteoSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

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