from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from Equipos.models import Equipo
from Jugadores.serializers import JugadorSerializer

class GetAllJugadoresView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):

        try:
            equipo = Equipo.objects.get(slug=slug)

            jugadores = equipo.jugadores.all()

            serializer = JugadorSerializer(jugadores, many=True)
            return Response(
                {"success": serializer.data},
                status= HTTP_200_OK)

        except Equipo.DoesNotExist:
            return Response(
                {"error": "Equipo no encontrado"},
                status=HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {"error": f'error{e}'},
                status=HTTP_500_INTERNAL_SERVER_ERROR
            )

