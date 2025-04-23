import secrets
from django.db import models

class Personaje(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    imagen = models.FileField(upload_to='media/personajes/', blank=True, null=True)

    class meta:
        verbose_name = 'Personaje'
        verbose_name_plural = 'Personajes'
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = secrets.token_urlsafe(16)
            while Personaje.objects.filter(slug=slug).exists():
                slug = secrets.token_urlsafe(16)
            self.slug = slug
        super().save(*args, **kwargs)




