from rest_framework import viewsets
from .models import Usuario, Publicacion, Etiqueta, Reposteo, Comentario
from .serializers import UsuarioSerializer, PublicacionSerializer, EtiquetaSerializer, ReposteoSerializer, ComentarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

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
