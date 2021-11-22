from rest_framework import views
from rest_framework.response import Response
from authApp.models.tiquetes import Tiquete
from authApp.serializers.tiqueteSerializer import CrearTiqueteSerializer, TiqueteSerializer


class TiqueteView(views.APIView):
    def get(self, request):
        lista_pasajero = Tiquete.objects.all()
        serializer = TiqueteSerializer(lista_pasajero, many=True)
        if not lista_pasajero:
            return Response({"mensaje": "no hay tiquetes"})
        print(serializer)
        return Response(serializer.data, 200)

    def post(self, request):
        datos_json = request.data
        serializer = CrearTiqueteSerializer(data=datos_json)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Se ha creado el tiquete"}, 200)
        else:
            return Response(serializer.errors, 405)

    def delete(self, request, pk):
        try:
            tiquete = Tiquete.objects.get(id=pk)
            tiquete.delete()
            return Response({"mensaje": "tiquete borrado"}, 200)
        except:
            return Response({"mensaje": "tiquete no existe"}, 400)