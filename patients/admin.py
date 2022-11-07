from django.contrib import admin
from django.urls import reverse
from .models import Patient, SessionPatient
from ventes.models import FactureVente
from django.utils.html import format_html


class FactureVenteInline(admin.TabularInline):
    model = FactureVente
    fields = [
        "_numero_de_facture",
        "type_de_facture",
        "date",
        "montant",
        "mode_de_reglement",
        "date_du_reglement",
        "statut_de_paiement",
        "_document_lie",
    ]
    readonly_fields = ["_document_lie", "_numero_de_facture"]
    show_change_link = True
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    def _document_lie(self, obj):
        human_readable_name = obj.document_lie.name.split("/")[-1]
        return format_html(
            f'<a href="{obj.document_lie.url}">{human_readable_name}</a>'
        )

    def _numero_de_facture(self, obj):
        """Return a link to change the object"""
        object_link = reverse(
            "admin:{0}_{1}_change".format(obj._meta.app_label, obj._meta.model_name),
            args=(obj.pk,),
        )
        return format_html(f'<a href="{object_link}">{obj.numero_de_facture}</a>')


class SessionPatientInline(admin.TabularInline):
    model = SessionPatient
    extra = 0
    show_change_link = True

    def has_change_permission(self, request, obj=None):
        return False


class PatientAdmin(admin.ModelAdmin):

    # Display related bills with tabular inlines
    inlines = [FactureVenteInline, SessionPatientInline]

    list_display = (
        "nom",
        "prenom",
        "sexe",
        "categorie",
        "date_naissance",
        "adresse",
        "telephone",
        "email",
        "_compte_rendu",
    )
    list_filter = ("sexe", "categorie")
    search_fields = ("nom", "prenom")
    ordering = ("nom",)

    def _compte_rendu(self, obj: Patient):
        if obj.compte_rendu:
            human_readable_name = obj.compte_rendu.name.split("/")[-1]
            return format_html(
                f'<a href="{obj.compte_rendu.url}">{human_readable_name}</a>'
            )
        else:
            return None


class SessionPatientAdmin(admin.ModelAdmin):
    list_display = ("date", "patient", "notes", "prestation", "facture_liee")
    search_fields = (
        "patient__nom",
        "patient__prenom",
        "facture_liee__numero_de_facture",
    )
    date_hierarchy = "date"
    ordering = ("-date",)


admin.site.register(Patient, PatientAdmin)
admin.site.register(SessionPatient, SessionPatientAdmin)
