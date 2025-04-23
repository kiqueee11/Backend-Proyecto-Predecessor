from django.db import models

from Jugadores.models import Jugador
from Redes.models import RedSocial


class RedesJugador(models.Model):
    link = models.CharField(max_length=300, verbose_name="Link de la red social", null=True, blank=True)
    jugador = models.ForeignKey(Jugador, related_name="red_social", null=False, blank=False, on_delete=models.RESTRICT)
    red = models.ForeignKey(RedSocial, related_name="redes_jugador", null=False, blank=False, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "redes_jugador"
        verbose_name = "Red_jugador"
        verbose_name_plural = "Redes_jugador"

    def __str__(self):
        return self.link