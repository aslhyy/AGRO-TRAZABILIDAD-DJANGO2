from django.db import models

# Create your models here.
from .mod_transporte import Transporte
from .mod_destinos import Destino

__all__ = ["Transporte", "Destino"]
