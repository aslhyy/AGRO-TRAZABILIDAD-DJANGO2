# procesos/mod_procesos.py
from django.db import models
from rest_framework import serializers, generics

# MODELO (con FK tal como pediste: referencia a lotes.Lote)
class Proceso(models.Model):
    lote = models.ForeignKey("lotes.Lote", on_delete=models.CASCADE)  # FK exacto
    tipo = models.CharField(max_length=50)
    fecha = models.DateField()
    duracion_min = models.IntegerField()

    def __str__(self):
        return f"{self.tipo} - Lote {self.lote_id}"

# SERIALIZER
class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields = "__all__"

# VISTAS (clases que importará config/urls.py)
class ProcesoListCreateView(generics.ListCreateAPIView):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer

class ProcesoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer
