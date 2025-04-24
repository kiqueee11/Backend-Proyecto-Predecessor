from django.views import View
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from Partidas.models import Partida
from Partidas.serializers import PartidaSerializer


class GetPartidas(APIView):
    permission_classes = [AllowAny,]

    def get(self, request):
        partidas = Partida.objects.all()
        serializer = PartidaSerializer(partidas, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

