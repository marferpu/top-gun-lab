from rest_framework import serializers
from .models import Usuario, Publicacion, Etiqueta, Reposteo, Comentario




class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class ReposteoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reposteo
        fields = '__all__'
