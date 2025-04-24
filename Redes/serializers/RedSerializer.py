from rest_framework import serializers

from Redes.models import RedSocial
from RedesJugadores.serializers import RedJugadorSerializer


class RedSocialSerializer(serializers.ModelSerializer):

    redes_jugador = RedJugadorSerializer(many=True, read_only=True)

    class Meta:
        model = RedSocial
        fields = ["nombre", "icono", "redes_jugador", "link"]
