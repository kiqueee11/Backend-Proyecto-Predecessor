from django.shortcuts import render

from Equipos.models import Equipo
from Equipos.serializers import serializadorCrearEquipo, serializadorEquipo
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateEquipoView(APIView):
    
    def post(self, request):
        data = request.data

        serializer = serializadorCrearEquipo(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"succes":"Equipo creado correctamente", "data": serializer.data}, status=201)
        else:
            return Response({"error":serializer.errors}, status=400)
    
class GetAllEquiposView(APIView):
    
    def get(self, request):
        equipos = Equipo.objects.all()
        serializer = serializadorEquipo(equipos, many=True)
        return Response({"succes":"Equipos encontrados","data": serializer.data}, status=200)