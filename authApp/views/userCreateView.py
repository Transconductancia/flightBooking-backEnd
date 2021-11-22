from rest_framework import status,views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):

    def post(self,request,*args,**kwargs):   

        #La entrada o datos del servicio web entran por aqui
     
        #en esta vista se crea un POST (un metod HTTP)
        #colocar el metodo http que necesito #el request es una data que el va recibir en el 
        #  cuerpo del JSON
        #args: argumentos basicos del servicio web  y **kwargs:cualquier otro argumento que se necsite (argumentos que no se sabe si puedan llegar pero pueden llegar)
        #lo minimo es que el POST siempre viene con un request en el body
        serializer=UserSerializer(data=request.data) #X
        serializer.is_valid(raise_exception=True) #si la data corresponde con lo del modelo no va a sacar ninguna excepción o si no me saca un mensaje que me dice que falló con un campo,no el tipo de dato aporpiado,el lanza una expecion para que yo no guarde cosas incorrectas 
        serializer.save()   # y guardemelo en la BD

        tokenData={"username":request.data["username"],
                   "password":request.data["password"]}
        tokenSerializer=TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data,status=status.HTTP_201_CREATED)