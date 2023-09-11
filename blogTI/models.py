from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
# from PIL import Image
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
def user_directory_path(instance, filename):
    return 'blogTI/{0}/{1}'.format(instance.title, filename)

class Publicacion(models.Model):
    
    options = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado')
    )
    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='publicado')

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    title = models.CharField(max_length=70, blank=True)
    content = models.TextField(max_length=1000)
    publication_date = models.DateTimeField(auto_now=True)
    num_reaction = models.PositiveIntegerField(default=0)
    num_repost = models.PositiveIntegerField(default=0)
    num_comments = models.PositiveIntegerField(default=0)
    # thumbnail = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    slug = models.SlugField(max_length=25, unique_for_date='publication_date', unique=True)
    # published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default='borrador')
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-publication_date',)

    def __str__(self):
        return "Post title: " + self.title + ", By: " + self.user_id.username

def nueva_url(instance, url=None):
    slug = slugify(instance.content)
    if url is not None:
        slug = url
    return slug

def url_ok(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = nueva_url(instance)
pre_save.connect(url_ok, sender=Publicacion)

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