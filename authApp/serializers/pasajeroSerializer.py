from authApp.models.pasajero import Pasajero
from rest_framework import serializers

class CrearPasajeroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pasajero
        fields = ['cedula', 'nombre', 'celular', 'correo', 'userP']

class MostarPasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = ['id', 'cedula', 'nombre', 'celular', 'correo']
