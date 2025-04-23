import secrets

from django.db import models


class Partida(models.Model):
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    fecha = models.DateTimeField(verbose_name='Fecha')



    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_urlsafe(16)
            while Partida.objects.filter(slug=prov).exists():
                prov = secrets.token_urlsafe(16)
            self.slug = prov
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fecha}"
