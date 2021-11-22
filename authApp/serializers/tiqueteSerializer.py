from authApp.models.tiquetes import Tiquete
from rest_framework import serializers
#se trae un serializador para la cuenta,entonces la Clase "AccountSerializer"va heredar de "ModelSerializer" asi se hace la herencia en Python
class TiqueteSerializer(serializers.ModelSerializer):
    #Ahora le generalización de la clase con un "class Meta" inetrno
    #se recomienda no recibir ni responder con informacion unica o que se autogenera  o foraneas por tema de seguridad solo se trabajrá con  'balance','lastChangeDate','isActive'
    class Meta:
        model = Tiquete
        fields = ['id', 'vuelo', 'pasajero', 'user']
        
class CrearTiqueteSerializer(serializers.ModelSerializer):
    #Ahora le generalización de la clase con un "class Meta" inetrno
    #se recomienda no recibir ni responder con informacion unica o que se autogenera  o foraneas por tema de seguridad solo se trabajrá con  'balance','lastChangeDate','isActive'
    class Meta:
        model = Tiquete
        fields = ['vuelo', 'pasajero', 'user']