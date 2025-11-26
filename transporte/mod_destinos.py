from django.db import models
from .mod_transporte import Transporte

class Destino(models.Model):
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, related_name="destinos")
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    hora_llegada_estimada = models.DateTimeField()

    def __str__(self):
        return f"Destino {self.ciudad} ({self.transporte.placa})"
