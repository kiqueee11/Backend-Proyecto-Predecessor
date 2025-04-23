from rest_framework import serializers

from Jugadores.models import Jugador
from Redes.serializers.RedSerializer import RedSocialSerializer


class JugadorSerializer(serializers.ModelSerializer):
    redes = RedSocialSerializer(many=True, read_only=True)

    class Meta:
        model = Jugador
        fields = '__all__'
