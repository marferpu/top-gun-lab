from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, PublicacionViewSet, EtiquetaViewSet, ReposteoViewSet, ComentarioViewSet
from .views import prueba_cache
from . import views

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'publicaciones', PublicacionViewSet)
router.register(r'etiquetas', EtiquetaViewSet)
router.register(r'reposteos', ReposteoViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', views.home),
    path('', include(router.urls)),
    path('prueba/', prueba_cache, name='prueba_cache'), #ruta de la caché, http://localhost:8000/blogTI/prueba/
    #path('registrarPublicacion/', views.registrarPublicacion),
    path('edicionPublicacion/<id>', views.edicionPublicacion),
    path('editarPublicacion/<id>', views.editarPublicacion),
    path('eliminarPublicacion/<id>', views.eliminarPublicacion),
    path('login', views.login)
]
