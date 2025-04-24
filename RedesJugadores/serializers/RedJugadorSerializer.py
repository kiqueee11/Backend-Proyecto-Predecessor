from rest_framework import serializers

from Redes.models import RedSocial
from RedesJugadores.models import RedesJugador


class RedJugadorSerializer(serializers.ModelSerializer):
    red = serializers.PrimaryKeyRelatedField(queryset=RedSocial.objects.all())
    red_nombre = serializers.CharField(source='red.nombre', read_only=True)
    red_icono = serializers.ImageField(source='red.icono', read_only=True)

    class Meta:
        model = RedesJugador
        fields = ["red", "link", "red_nombre", "red_icono"]