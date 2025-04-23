from Equipos.models import Equipo
from rest_framework import serializers

class serializadorCrearEquipo(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
    
    def validate(self, data):
        if not data.get('nombre'):
            raise serializers.ValidationError("El nombre del equipo es obligatorio")
        return data
        
class serializadorEquipo(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
