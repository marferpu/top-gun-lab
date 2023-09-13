from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required

from .models import Publicacion, Etiqueta, Reposteo, Comentario
from .serializers import PublicacionSerializer, EtiquetaSerializer, ReposteoSerializer,ComentarioSerializer, UserSerializer
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

def inicio(request):
    return render(request, "inicio.html")

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

class BlogListView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Publicacion.objects.all()
        serializer = PublicacionSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetailView(APIView):
    def get(self, request, post_slug, *args, **kwargs):
        post = Publicacion.objects.get(slug=post_slug)
        serializer = PublicacionSerializer(post)
        return Response(serializer.data)

@api_view(['POST'])
def crear_publicacion(request):
    serializer = PublicacionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return redirect('/blogTI')

@api_view(['PUT'])
def editar_publicacion(request, id):
    usuario_autenticado = request.user
    try:
        post = Publicacion.objects.get(id=post.id)
    except Publicacion.DoesNotExist:
        return Response({'message': 'Publicación no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    if post.user_id != usuario_autenticado:
        return Response({'message': 'No tienes permiso para editar esta publicación'}, status=status.HTTP_403_FORBIDDEN)

    serializer = PublicacionSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return render(request, 'edicionPublicacion.html', {"mensaje": "Publicación editada exitosamente"}) 
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def eliminar_publicacion(request, id):
#     usuario_autenticado = request.user  
#     try:
#         post = Publicacion.objects.get(id=post.id)
#     except Publicacion.DoesNotExist:
#         return Response({'message': 'Publicación no encontrada'}, status=status.HTTP_404_NOT_FOUND)

#     if post.user_id != usuario_autenticado:
#         return Response({'message': 'No tienes permiso para eliminar esta publicación'}, status=status.HTTP_403_FORBIDDEN)
#     post.delete()
#     # return Response(status=status.HTTP_204_NO_CONTENT)
#     return redirect('/blogTI')

def eliminarPublicacion(request, id):
    publicacion = Publicacion.objects.get(id=id)
    publicacion.delete()

    messages.success(request, '¡Publicación eliminada!')

    return redirect('/blogTI')

# #implementación de redis
def prueba_cache(request):

    cache.set("my_key", "Hello World", 600)

    value = cache.get("my_key")

    return HttpResponse("La cache fue creada y consultada")

# # prueba crud

def home(request):
    publicacionListados = Publicacion.objects.all()
    messages.success(request, '¡Publicaciones listadas!')
    return render(request, "gestionPost.html", {"Publicacion": publicacionListados})

# @login_required
# def profile(request):
#     user = request.user
    
#     username = user.username
#     email = user.email
#     date_joined = user.date_joined
#     # country = user.country
#     context = {
#         'username': username,
#         'email': email,
#         'date_joined': date_joined,
#         # 'country': country
#     }  
#     return render(request, 'profile.html', context)
# def registrarPublicacion(request):
#     user_id = request.POST['user_id']
#     title = request.POST['title']
#     content = request.POST['content']

#     publicacion = Publicacion.objects.create(
#         user_id=user_id,title=title, content=content
#         #, num_reaction=num_reaction, num_repost=num_repost,num_comments=num_comments
#          )
#     messages.success(request, '¡Publicación registrada!')
#     return redirect('/blogTI')


#     messages.success(request, '¡Publicación actualizada!')

#     return redirect('/blogTI')
