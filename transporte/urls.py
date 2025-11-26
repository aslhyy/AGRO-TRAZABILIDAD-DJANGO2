from django.urls import path
from .views import (
    TransporteListCreateView,
    TransporteRetrieveUpdateDeleteView,
    DestinoListCreateView,
    DestinoRetrieveUpdateDeleteView,
    RutasActivasView,
)

urlpatterns = [
    # Transporte CRUD
    path("", TransporteListCreateView.as_view(), name="transporte-list-create"),
    path("<int:pk>/", TransporteRetrieveUpdateDeleteView.as_view(), name="transporte-detail"),

    # Destinos CRUD
    path("destinos/", DestinoListCreateView.as_view(), name="destinos-list-create"),
    path("destinos/<int:pk>/", DestinoRetrieveUpdateDeleteView.as_view(), name="destino-detail"),

    # Rutas activas
    path("rutas/activas/", RutasActivasView.as_view(), name="rutas-activas"),
]
