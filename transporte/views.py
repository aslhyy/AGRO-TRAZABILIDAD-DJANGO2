from django.shortcuts import render
from django.utils import timezone


# Create your views here.
from rest_framework import generics
from .models import Transporte, Destino
from .serializers import TransporteSerializer, DestinoSerializer

# CRUD TRANSPORTE
class TransporteListCreateView(generics.ListCreateAPIView):
    queryset = Transporte.objects.all()
    serializer_class = TransporteSerializer


class TransporteRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transporte.objects.all()
    serializer_class = TransporteSerializer


# CRUD DESTINOS
class DestinoListCreateView(generics.ListCreateAPIView):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer


class DestinoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer


# Rutas activas → transportes sin llegada
class RutasActivasView(generics.ListAPIView):
    serializer_class = TransporteSerializer

    def get_queryset(self):
        hoy = timezone.now().date()
        return (
            Transporte.objects
            .filter(fecha_llegada__isnull=False)  # Sigue siendo una ruta activa
            .filter(fecha_salida__gt=timezone.now())  # Y solo si sale después del día actual
        )
