from django.http.response import JsonResponse
from rest_framework import views
from rest_framework.response import Response
from authApp.models.pasajero import Pasajero
from authApp.serializers.pasajeroSerializer import MostarPasajeroSerializer 
from authApp.serializers.pasajeroSerializer import CrearPasajeroSerializer


class PasajeroView(views.APIView):
    def get(self, request):
        lista_pasajero = Pasajero.objects.all()
        serializer = MostarPasajeroSerializer(lista_pasajero, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        datos_json = request.data
        serializer = CrearPasajeroSerializer(data=datos_json)
        if serializer.is_valid():
            serializer.save()
            ultimo_pasajero = Pasajero.objects.last()
            serializer_ultimo_pasajero = MostarPasajeroSerializer(ultimo_pasajero, many=False)
            return Response(serializer_ultimo_pasajero.data, 200)
        else:
            return Response(serializer.errors, 405)

    def delete(self, request, pk):
        try:
            pasajero = Pasajero.objects.get(pk=pk)
            pasajero.delete()
            return Response({"mensaje": "Pasajero borrado"}, 200)
        except:
            return Response({"mensaje": "Pasajero no existe"}, 400)