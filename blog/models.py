from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Slug')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Categoría')
    body = models.TextField(verbose_name='Contenido')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Autor')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-id']

    def __str__(self):
        return self.title
