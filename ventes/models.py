from django.db import models


class Prestation(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Prestation"
        verbose_name_plural = "Prestations"
        ordering = ["nom"]


class FactureVente(models.Model):
    numero_de_facture = models.CharField(max_length=100, unique=True)
    type_de_facture = models.CharField(
        max_length=2,
        choices=[("FD", "Facture définitive"), ("A", "Facture d'Acompte")],
        default="FD",
        help_text=(
            "Note : les factures d'acompte se font à la date"
            " de réception du paiement"
        ),
    )
    date = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE)
    prestations = models.ManyToManyField(Prestation)
    mode_de_reglement = models.CharField(
        max_length=2,
        choices=[
            ("ES", "Espèces"),
            ("CH", "Chèque"),
            ("VI", "Virement"),
            ("CB", "Carte bancaire"),
        ],
    )
    date_du_reglement = models.DateField(blank=True, null=True)
    statut_de_paiement = models.CharField(
        max_length=2, choices=[("RE", "Reçu"), ("EN", "En attente"), ("AN", "Annulé")]
    )
    document_lie = models.FileField(
        upload_to="ventes/documents/factures_de_ventes", blank=True, null=True
    )

    def __str__(self):
        return f"{self.numero_de_facture} - {self.patient}"
