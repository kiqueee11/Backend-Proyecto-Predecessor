import secrets
from django.db import models

class Equipo(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=100, unique=True)
    victorias = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)
    winrate = models.FloatField(default=0.0)
    imagen = models.FileField(upload_to='media/equipos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['winrate']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = secrets.token_urlsafe(16)
            while Equipo.objects.filter(slug=slug).exists():
                slug = secrets.token_urlsafe(16)
            self.slug = slug
        super().save(*args, **kwargs)
    
    def calcular_winrate(self):
        if self.victorias + self.derrotas > 0:
            self.winrate = (self.victorias / (self.victorias + self.derrotas)) * 100
        else:
            self.winrate = 0.0
        self.save()
    
    def __str__(self):
        return self.nombre
