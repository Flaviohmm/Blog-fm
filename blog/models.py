from typing import Iterable

from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Nome do ícone (ex: terminal, cpu, treding-up)")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering =['name']

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(max_length=220, unique=True)

    content = CKEditor5Field(
        'Conteúdo',
        config_name='default',
    )

    # Relacionamentos
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Categoria"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    # Informações do post
    featured_image = models.ImageField(
        upload_to='posts/%Y/%m/',
        blank=True,
        null=True,
        verbose_name="Imagem destacada"
    )

    is_tutorial = models.BooleanField(default=False, verbose_name="É um tutorial?")
    read_time = models.PositiveIntegerField(default=5, help_text="Tempo estimado de leitura em minutos")

    # Links externos
    github_link = models.URLField(blank=True, null=True, verbose_name="Link do GitHub")

    # Status e datas
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Data de publicação")
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0, editable=False)

    # SEO
    meta_description = models.TextField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=['-published_at']),
            models.Index(fields=['slug'])
        ]

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_read_time_display(self):
        return f"{self.read_time} min de leitura"
    

# Modelo auxiliar para destacar tópicos
class Topic(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, help_text="Ex: terminal, cpu, trending-up, shield, globe")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Tópico"
        verbose_name_plural = "Tópicos"

    def __str__(self) -> str:
        return self.title
    