from django.db import models
from .user import User
from .pasajero import Pasajero
from .vuelo import Vuelo


class Tiquete(models.Model):
    id = models.AutoField(primary_key=True)
    vuelo = models.ForeignKey(Vuelo, null=False, blank=False,on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, null=False, blank=False,on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False,on_delete=models.CASCADE)