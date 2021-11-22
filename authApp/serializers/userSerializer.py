from rest_framework import serializers
from authApp.models.user import User         #acá es una llave primaria
# la anterior es ruta absoluta o tambien podia ser con ruta relativa from .accountSerializer import AccountSerializer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password','name','email'] #JSON
     
     #aqui entre serialaizer y vista van a ser el controlador o sea es el intermediario para #crear un nuevo usuario#aqui vamamos a crear un usuario..y creamos una funcion que permite #llamar a la creacion 

     #OBJETO y guardo eso 
    def create(self,validated_data):  # "validated_data" es informacion que nos llega de   un    #formulario ya validado en forma de diccionario (es casi un JSON)
        #vamos a tener información propia de la #cuenta, en esste caso del campo "account" que est ahi arriba en field
        #"validated_data" es un JSON uan informacion que yo recibí y la voy a pasar a objeto
      
        userInstance=User.objects.create(**validated_data)#por lo tanto creo un ojeto de tipo usuario
        # aui está el ORM enlazando # con los  CREATE ya estamos guardadndo por defecto los dos objetos 
        return userInstance

        # el "to_representative" es como el ToString de Java
        #aqui defino la estructura del servicio y lo que quiero responder 
        #esto lo estoy recibiendo del sitio WEB

        #retorno del JSON
    def to_representation(self,obj):        #este "obj" es parcticamente el objeto que acabamos de crear  
        user=User.objects.get(id=obj.id)    #traigame el usuario que corresponde a ese id y guardemelo en la varibale "user"
        #GET es como un SELECT con este where "(user=obj.id)"
        #traigame todas las cuentas que corresponden a esta llave foranea y guardelas aqui en la variable "account"
        # vean que no se utiliza SELECT sino GET por tanto ya no se escribe SQL sino funciones genericas
        return{   #esto es lo que quiero RETORNAR o REGRESAR  en su servicio WEB pero tambien esta el de iDA
                 'id':user.id,
                 'username':user.username,
                 'name':user.name,
                 'email':user.email,
              }

