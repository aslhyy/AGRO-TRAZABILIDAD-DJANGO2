# procesos/mod_procesos.py
from django.db import models

# MODELO (con FK tal como pediste: referencia a lotes.Lote)
class Proceso(models.Model):
    lote = models.ForeignKey("lotes.Lote", on_delete=models.CASCADE)  # FK exacto
    tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    duracion_min = models.IntegerField()

    def __str__(self):
        return f"{self.tipo} - Lote {self.lote_id}"
