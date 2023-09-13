from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PublicacionViewSet, EtiquetaViewSet, ReposteoViewSet, ComentarioViewSet
from .views import PublicacionViewSet, BlogListView, PostDetailView
from .views import prueba_cache
from . import views

app_name="blogTI"
router = DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'publicaciones', PublicacionViewSet)
router.register(r'etiquetas', EtiquetaViewSet)
router.register(r'reposteos', ReposteoViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('login', views.login),
    path('', views.home),
    path('', include(router.urls)),
    path('eliminarPublicacion/<id>', views.eliminarPublicacion),
    path('editar_publicacion/<id>', views.editar_publicacion),
    # path('posts/', BlogListView.as_view()),
    # path('posts/<post_slug>', PostDetailView.as_view()),
    # path('publicaciones/<id>', views.editar_publicacion, name='editar_publicacion'),
    # path('publicaciones/<id>', views.eliminar_publicacion, name='eliminar_publicacion'),
    # path('crear_publicacion/', views.crear_publicacion, name='crear_publicacion'),

    # path('profile/', views.profile, name='profile'),

    path('prueba/', prueba_cache, name='prueba_cache'), #ruta de la caché, http://localhost:8000/blogTI/prueba/
    #path('registrarPublicacion/', views.registrarPublicacion),
    # path('edicionPublicacion/<id>', views.edicionPublicacion),
    # path('editarPublicacion/<id>', views.editarPublicacion),
    # path('eliminarPublicacion/<id>', views.eliminarPublicacion),
    
]
