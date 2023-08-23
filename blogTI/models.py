from django.db import models

# Create your models here.
class Usuario(models.Model):

    fullname = models.CharField(max_length=70)
    email = models.EmailField(blank=True)
    country = models.CharField(max_length=70) #falta organizar la parte de selección del pais
    password = models.CharField(max_length=70)
    registration_date = models.DateTimeField(auto_now=True)

class Publicacion(models.Model):

    user_id = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    title = models.EmailField(blank=True)
    content = models.CharField(max_length=70)
    publication_date = models.DateTimeField(auto_now=True)
    num_reaction = models.PositiveIntegerField()
    num_repost = models.PositiveIntegerField()
    num_comments = models.PositiveIntegerField()

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
