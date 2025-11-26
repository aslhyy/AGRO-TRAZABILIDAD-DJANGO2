from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lote, HistorialLote
from .serializers import HistorialLoteSerializer


class HistorialPorLoteView(generics.ListAPIView):
    serializer_class = HistorialLoteSerializer

    def get_queryset(self):
        lote_id = self.kwargs["lote_id"]
        return HistorialLote.objects.filter(lote_id=lote_id).order_by("fecha")


class TrazabilidadCompletaView(APIView):
    def get(self, request, lote_id):
        try:
            lote = Lote.objects.get(id=lote_id)
        except Lote.DoesNotExist:
            return Response({"error": "Lote no encontrado"}, status=404)

        # Información principal del lote
        lote_data = {
            "id": lote.id,
            "cultivo": lote.cultivo,
            "estado": lote.estado,
            "fecha_siembra": lote.fecha_siembra,
        }

        # Historial real del lote
        historial = HistorialLote.objects.filter(lote=lote).order_by("fecha")
        historial_data = HistorialLoteSerializer(historial, many=True).data

        # Trazabilidad solo con datos reales
        return Response({
            "lote": lote_data,
            "historial": historial_data,
        })
