from django.urls import path
from .mod_lotes import (
    LoteListCreateView,
    LoteRetrieveUpdateDeleteView,
)
from .mod_trazabilidad import (
    HistorialPorLoteView,
    TrazabilidadCompletaView,
)

urlpatterns = [
    # LOTES CRUD
    path("", LoteListCreateView.as_view(), name="lotes-list-create"),
    path("<int:pk>/", LoteRetrieveUpdateDeleteView.as_view(), name="lote-detail"),

    # HISTORIAL POR LOTE
    path("<int:lote_id>/historial/", HistorialPorLoteView.as_view(), name="lote-historial"),

    # TRAZABILIDAD COMPLETA
    path("<int:lote_id>/trazabilidad/", TrazabilidadCompletaView.as_view(), name="lote-trazabilidad"),
]
