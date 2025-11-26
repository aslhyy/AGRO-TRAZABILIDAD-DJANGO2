from django.db import models

class Lote(models.Model):
    cultivo = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    fecha_siembra = models.DateField()

    def __str__(self):
        return f"Lote {self.id} - {self.cultivo}"


class HistorialLote(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, related_name="historial")
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    etapa = models.CharField(max_length=100)

    def __str__(self):
        return f"Historial Lote {self.lote.id} - {self.etapa}"
