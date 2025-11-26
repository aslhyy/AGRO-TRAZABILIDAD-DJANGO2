from django.db import models

# Create your models here.
# procesos/models.py
from .mod_procesos import Proceso
from .mod_detalles import DetalleProceso

__all__ = ["Proceso", "DetalleProceso"]
