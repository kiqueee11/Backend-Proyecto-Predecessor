import secrets

from django.db import models

from Equipos.models import Equipo
from Personajes.models import Personaje

class Partida(models.Model):
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    fecha = models.DateTimeField(verbose_name='Fecha')
    equipo1 = models.ForeignKey(Equipo, on_delete=models.CASCADE, verbose_name='Equipo 1', related_name='equipo1', null=True, blank=True)
    equipo2 = models.ForeignKey(Equipo, on_delete=models.CASCADE, verbose_name='Equipo 2', related_name='equipo2', null=True, blank=True)
    primer_equipo_elegir = models.CharField( max_length=100, verbose_name='Primer equipo en elegir', blank=True, null=True)
    ganador = models.CharField(max_length=100,choices=[],verbose_name='Ganador',blank=True,null=True)
    personajes_baneados = models.ManyToManyField(Personaje, verbose_name='Personajes baneados', blank=True, related_name="baneado_en")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        db_table = 'Partidas'
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_urlsafe(16)
            while Partida.objects.filter(slug=prov).exists():
                prov = secrets.token_urlsafe(16)
            self.slug = prov

        self._meta.get_field('primer_equipo_elegir').choices = self.get_equipo_choices()
        self._meta.get_field('ganador').choices = self.get_equipo_choices()
        super().save(*args, **kwargs)

    def get_equipo_choices(self):
        return [
            (self.equipo1.nombre, self.equipo1.nombre),
            (self.equipo2.nombre, self.equipo2.nombre)
        ]

    def __str__(self):
        return f"{self.fecha}"
