from django.db import models

class Transporte(models.Model):
    placa = models.CharField(max_length=20, unique=True)
    conductor = models.CharField(max_length=100)
    temperatura = models.FloatField()
    fecha_salida = models.DateTimeField()
    fecha_llegada = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Transporte {self.placa}"
