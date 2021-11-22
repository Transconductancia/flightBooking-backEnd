from authApp.models.vuelo import Vuelo
from rest_framework import serializers
#se trae un serializador para la cuenta,entonces la Clase "AccountSerializer"va heredar de "ModelSerializer" asi se hace la herencia en Python
class VueloSerializer(serializers.ModelSerializer):
    #Ahora le generalizaci�n de la clase con un "class Meta" inetrno
    #se recomienda no recibir ni responder con informacion unica o que se autogenera  o foraneas por tema de seguridad solo se trabajr� con  'balance','lastChangeDate','isActive'
    class Meta:
        model = Vuelo
        fields = ['fecha', 'sillas', 'ciudad_origen', 'ciudad_destino', 'user']
        
class MostarVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelo
        fields = ['id', 'fecha', 'sillas', 'ciudad_origen', 'ciudad_destino']
