from django.contrib import admin
from .models import User, Reposteo, Etiqueta, Publicacion, Comentario
# from comment.models import Comment
# Register your models here.
admin.site.register(Publicacion)
admin.site.register(Reposteo)
admin.site.register(Comentario)
admin.site.register(Etiqueta)