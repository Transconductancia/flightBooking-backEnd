from django.contrib import admin

from .models.user import User
from .models.pasajero import Pasajero
from .models.vuelo import Vuelo
from .models.tiquetes import Tiquete

# Register your models here.
admin.site.register(User)
admin.site.register(Pasajero)
admin.site.register(Vuelo)
admin.site.register(Tiquete)