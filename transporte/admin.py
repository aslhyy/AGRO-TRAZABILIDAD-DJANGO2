from django.contrib import admin

# Register your models here.

from .models import Transporte, Destino

admin.site.register(Transporte)
admin.site.register(Destino)
