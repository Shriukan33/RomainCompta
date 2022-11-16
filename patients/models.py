from django.db import models


class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, choices=[("M", "Masculin"), ("F", "Féminin")])
    categorie = models.CharField(
        max_length=1, choices=[("A", "Adulte"), ("E", "Enfant")]
    )
    date_naissance = models.DateField(verbose_name="Date de naissance")
    adresse = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    compte_rendu = models.FileField(
        upload_to="patients/documents/compte_rendu", blank=True, null=True
    )
    suivi = models.CharField(
        max_length=1,
        choices=[("Y", "En cours"), ("N", "Terminé")],
        default="Y",
    )

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        ordering = ["nom"]


class SessionPatient(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    prestation = models.ForeignKey("ventes.Prestation", on_delete=models.CASCADE)
    facture_liee = models.ForeignKey(
        "ventes.FactureVente", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.patient} - {self.date}"

    class Meta:
        verbose_name = "Session patient"
        verbose_name_plural = "Sessions patient"
        ordering = ["date"]
