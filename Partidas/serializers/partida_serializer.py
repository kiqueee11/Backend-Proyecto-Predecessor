from rest_framework import serializers

from Equipos.models import Equipo
from Partidas.models import Partida

class NestedEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('slug', 'nombre', 'imagen')

class PartidaSerializer(serializers.ModelSerializer):
    equipo1 = NestedEquipoSerializer()
    equipo2 = NestedEquipoSerializer()

    class Meta:
        model = Partida
        fields = ('slug', 'fecha', 'equipo1', 'equipo2', 'ganador', 'created_at', 'updated_at',)