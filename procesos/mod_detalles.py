# procesos/mod_detalles.py
from django.db import models

# MODELO (FK a procesos.Proceso)
class DetalleProceso(models.Model):
    proceso = models.ForeignKey("procesos.Proceso", on_delete=models.CASCADE)  # FK exacto
    descripcion = models.TextField()
    responsable = models.CharField(max_length=100)

    def __str__(self):
        return f"Detalle {self.id} - Proceso {self.proceso_id}"


