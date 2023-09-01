from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    country = models.CharField(max_length=100)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Publicacion(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, blank=True)
    content = models.CharField(max_length=1000)
    publication_date = models.DateTimeField(auto_now=True)
    num_reaction = models.PositiveIntegerField(default=0)
    num_repost = models.PositiveIntegerField(default=0)
    num_comments = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Post title: " + self.title + ", By: " + self.user_id.username

class Etiqueta(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    tag = models.CharField(max_length=5)

class Reposteo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

class Comentario(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now=True)
    total_comments = models.PositiveIntegerField(default=0)