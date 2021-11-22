from django.conf import settings
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.vuelo import Vuelo
from authApp.serializers.vueloSerializer import VueloSerializer

class VuelosDetailView(generics.RetrieveAPIView):
    queryset=Vuelo.objects.all()
    serializer_class=VueloSerializer
    permission_classes=(IsAuthenticated,)

    def get (self,request,*args,**kwargs):
   
        return super().get(request,*args,**kwargs)

