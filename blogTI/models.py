# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    country = models.CharField(max_length=50)

class Publicacion(models.Model):

    user_id = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, blank=True)
    content = models.CharField(max_length=1000, null=False)
    publication_date = models.DateTimeField(auto_now=True)
    num_reaction = models.PositiveIntegerField()
    num_repost = models.PositiveIntegerField()
    num_comments = models.PositiveIntegerField()
    def __str__(self) -> str:
        fila = "Post title: " + self.title +",  " +"By: " + self.user_id.fullname
        return fila

class Etiqueta(models.Model):

    user_id = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Publicacion, null=False, blank=False, on_delete=models.CASCADE)
    tag = models.CharField(max_length=5)

class Reposteo(models.Model):

    user_id = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Publicacion, null=False, blank=False, on_delete=models.CASCADE)

class Comentario(models.Model):

    user_id = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Publicacion, null=False, blank=False, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now=True)
    total_comments = models.PositiveIntegerField()
