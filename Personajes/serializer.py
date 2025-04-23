from Personajes.models import Personaje
from rest_framework import serializers


class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = ['id', 'nombre', 'slug', 'imagen']

    