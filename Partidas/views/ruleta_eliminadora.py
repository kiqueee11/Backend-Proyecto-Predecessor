import random

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

import Partidas
from Partidas.models import Partida
from Partidas.serializers import NestedEquipoSerializer
from Personajes.models import Personaje
from Personajes.serializer import PersonajeSerializer


class RuletaEliminadora(APIView):
    permission_classes = (AllowAny,)

    def get (self, request, slug):
        partida = get_object_or_404(Partida, slug=slug)

        personajes = list(Personaje.objects.all())
        personajes_baneados =  random.sample(personajes,10)
        personajes_restantes = list(set(personajes) - set(personajes_baneados))

        serializer_baneados = PersonajeSerializer(personajes_baneados, many=True)
        serializer_restantes = PersonajeSerializer(personajes_restantes, many=True)

        partida.personajes_baneados.clear()
        partida.personajes_baneados.add(*personajes_baneados)

        primer_equipo_elegir = random.choice([partida.equipo1, partida.equipo2])
        serializer_equipo = NestedEquipoSerializer(primer_equipo_elegir)

        partida.primer_equipo_elegir = primer_equipo_elegir.nombre
        partida.save()
        return Response({
            "primer_equipo_elegir": serializer_equipo.data,
            "personajes_baneados": serializer_baneados.data,
            "personajes_restantes": serializer_restantes.data},
            status=HTTP_200_OK)
