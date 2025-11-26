# procesos/mod_detalles.py
from django.db import models
from rest_framework import serializers, generics

# MODELO (FK a procesos.Proceso)
class DetalleProceso(models.Model):
    proceso = models.ForeignKey("procesos.Proceso", on_delete=models.CASCADE)  # FK exacto
    descripcion = models.TextField()
    responsable = models.CharField(max_length=100)

    def __str__(self):
        return f"Detalle {self.id} - Proceso {self.proceso_id}"

# SERIALIZER
class DetalleProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleProceso
        fields = "__all__"

# VISTAS
class DetalleProcesoListCreateView(generics.ListCreateAPIView):
    queryset = DetalleProceso.objects.all()
    serializer_class = DetalleProcesoSerializer

class DetalleProcesoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalleProceso.objects.all()
    serializer_class = DetalleProcesoSerializer
