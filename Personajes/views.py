from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from Personajes.models import Personaje
from Personajes.serializer import PersonajeSerializer

class GetAllPersonajesView(APIView):
    def get(self, request):
        personajes = Personaje.objects.all()
        serializer = PersonajeSerializer(personajes, many=True)
        return Response({"succes":"Personajes encontrados","data": serializer.data}, status=200)
        
