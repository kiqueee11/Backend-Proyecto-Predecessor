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
            equipo = serializer.save()
            equipo.calcular_winrate()
            return Response({"succes":"Equipo creado correctamente", "data": serializer.data}, status=201)
        else:
            return Response({"error":serializer.errors}, status=400)
    
class GetAllEquiposView(APIView):
    
    def get(self, request):
        equipos = Equipo.objects.all()
        serializer = serializadorEquipo(equipos, many=True)
        return Response({"succes":"Equipos encontrados","data": serializer.data}, status=200)
    
class UpdateEquipoView(APIView):
    
    def post(self, request, slug):
        try:
            equipo = Equipo.objects.get(slug=slug)
        except Equipo.DoesNotExist:
            return Response({"error":"Equipo no encontrado"}, status=404)

        data = request.data

        serializer = serializadorEquipo(instance=equipo, data=data, partial=True)
        
        if serializer.is_valid():
            equipo = serializer.save()
            equipo.calcular_winrate()
            return Response({"succes":"Equipo actualizado correctamente", "data": serializer.data}, status=201)
        else:
            return Response({"error":serializer.errors}, status=400)