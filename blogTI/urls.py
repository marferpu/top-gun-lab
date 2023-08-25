from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, PublicacionViewSet, EtiquetaViewSet, ReposteoViewSet, ComentarioViewSet


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'publicaciones', PublicacionViewSet)
router.register(r'etiquetas', EtiquetaViewSet)
router.register(r'reposteos', ReposteoViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls))
]
