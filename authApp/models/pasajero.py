from django.db import models
from django.db.models.fields import EmailField
from .user import User


class Pasajero(models.Model):
    
    class Meta:
        get_latest_by = 'id'
        
    id = models.BigAutoField(primary_key=True)
    cedula = models.IntegerField()
    nombre = models.CharField('Name', max_length= 50)
    celular = models.BigIntegerField()
    correo = models.EmailField('Email', max_length= 100)
    userP = models.ForeignKey(User, related_name='CreadorPasajero', on_delete=models.CASCADE)