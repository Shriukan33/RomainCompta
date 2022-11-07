from django.urls import path

from .views import CompteRenduView

urlpatterns = [
    path(
        "documents/compte_rendu/<str:filename>",
        CompteRenduView.as_view(),
        name="compte_rendu",
    ),
]
