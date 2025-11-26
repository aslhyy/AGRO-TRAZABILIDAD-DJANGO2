from rest_framework import generics
from django.utils import timezone

from .models import Lote, HistorialLote
from .serializers import LoteSerializer


class LoteListCreateView(generics.ListCreateAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        cultivo = self.request.query_params.get("cultivo")
        estado = self.request.query_params.get("estado")

        if cultivo:
            qs = qs.filter(cultivo__icontains=cultivo)

        if estado:
            qs = qs.filter(estado__iexact=estado)

        return qs


class LoteRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

    def perform_update(self, serializer):
        # 1. Guardar los cambios del lote
        lote = serializer.save()

        # 2. Crear registro en historial
        HistorialLote.objects.create(
            lote=lote,
            fecha=timezone.now(),
            descripcion=f"Actualización del lote {lote.id}",
            etapa=lote.estado,      # puedes cambiarlo si deseas guardar otro campo
        )
