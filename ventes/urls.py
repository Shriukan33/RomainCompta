from django.urls import path

from .views import FactureVenteView

urlpatterns = [
    path(
        "documents/factures_de_ventes/<str:filename>",
        FactureVenteView.as_view(),
        name="facture_vente",
    ),
]
