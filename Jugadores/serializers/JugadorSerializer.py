from rest_framework import serializers

from Jugadores.models import Jugador
from RedesJugadores.serializers import RedJugadorSerializer


class JugadorSerializer(serializers.ModelSerializer):
    red_social = RedJugadorSerializer(many=True, read_only=True)

    class Meta:
        model = Jugador
        fields = ["nombre", "nickname", "red_social"]
