from django.db import models
from django.db.models.fields import IntegerField
from django.contrib.postgres.fields import ArrayField
from .user import User
class Vuelo(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    sillas = ArrayField(IntegerField(), null=True)
    ciudad_origen = models.CharField('Origen', max_length = 50)
    ciudad_destino = models.CharField('Destino', max_length = 50)
    user = models.ForeignKey(User, related_name='CreadorVuelo', on_delete=models.CASCADE)