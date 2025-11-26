from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas LOTES
    path("api/lotes/", include("lotes.urls")),

    # PROCESOS
    path('api/procesos/', include("procesos.urls")),


    # TRANSPORTE (nueva app)
    path('api/transporte/', include('transporte.urls')),

    # Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
