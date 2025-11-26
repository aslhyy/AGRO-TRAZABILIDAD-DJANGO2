from django.urls import path
from .views import (
    ProcesoListCreateView,
    ProcesoRetrieveUpdateDeleteView,
    DetalleProcesoListCreateView,
    DetalleProcesoRetrieveUpdateDeleteView,
)

urlpatterns = [
    # PROCESOS
    path('', ProcesoListCreateView.as_view(), name='procesos-list'),
    path('<int:pk>/', ProcesoRetrieveUpdateDeleteView.as_view(), name='procesos-detail'),

    # DETALLES
    path('detalles/', DetalleProcesoListCreateView.as_view(), name='detalles-list'),
    path('detalles/<int:pk>/', DetalleProcesoRetrieveUpdateDeleteView.as_view(), name='detalles-detail'),
]
