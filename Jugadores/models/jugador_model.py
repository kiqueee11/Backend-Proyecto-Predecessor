import secrets

from django.db import models
from django.db.models import ManyToManyField, ForeignKey

from Equipos.models import Equipo
from Redes.models import RedSocial


class Jugador(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del jugador")
    nickname = models.CharField(unique=True, null=False, blank=False, verbose_name="Nickname en el juego")
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    equipo = ForeignKey(Equipo, on_delete=models.SET_NULL, related_name="jugadores", verbose_name="Equipo del jugador", null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "jugadores"
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_urlsafe(16)
            while Jugador.objects.filter(slug=prov).exists():
                prov = secrets.token_urlsafe(16)
            self.slug = prov
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nickname