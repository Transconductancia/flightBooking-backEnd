from rest_framework import views
from rest_framework.response import Response
from authApp.models.vuelo import Vuelo
from authApp.serializers.vueloSerializer import MostarVueloSerializer 
from authApp.serializers.vueloSerializer import VueloSerializer


class VueloView(views.APIView):
    def get(self, request):
        lista_vuelo = Vuelo.objects.all()
        serializer = MostarVueloSerializer(lista_vuelo, many=True)
        if not lista_vuelo:
            return Response({"mensaje": "no hay vuelos"})
        return Response(serializer.data, 200)

    def post(self, request):
        datos_json = request.data
        serializer = VueloSerializer(data=datos_json)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Se a creado el vuelo"}, 200)
        else:
            return Response(serializer.errors, 405)

    def delete(self, request, pk):
        try:
            vuelo = Vuelo.objects.get(id=pk)
            vuelo.delete()
            return Response({"mensaje": "Vuelo borrado"}, 200)
        except:
            return Response({"mensaje": "vuelo no existe"}, 400)