from django.contrib import admin
from .models import Usuario, Publicacion, Reposteo, Comentario, Etiqueta
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Publicacion)
admin.site.register(Reposteo)
admin.site.register(Comentario)
admin.site.register(Etiqueta)