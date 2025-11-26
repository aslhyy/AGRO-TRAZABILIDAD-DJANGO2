from rest_framework import generics
from .models import Proceso, DetalleProceso
from .serializers import ProcesoSerializer, DetalleProcesoSerializer


# PROCESOS
class ProcesoListCreateView(generics.ListCreateAPIView):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer


class ProcesoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer


# DETALLES
class DetalleProcesoListCreateView(generics.ListCreateAPIView):
    queryset = DetalleProceso.objects.all()
    serializer_class = DetalleProcesoSerializer


class DetalleProcesoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalleProceso.objects.all()
    serializer_class = DetalleProcesoSerializer
