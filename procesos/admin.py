from django.contrib import admin
from .models import Proceso, DetalleProceso

# Registro sencillo al estilo del admin.py que usaste para Lote
admin.site.register(Proceso)
admin.site.register(DetalleProceso)
