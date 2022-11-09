from django.contrib import admin
from admincharts.admin import AdminChartMixin
from django.utils.html import format_html
from .models import FactureVente, Prestation
from django.db.models import QuerySet, Sum
from django.db.models.functions import TruncMonth
from django.utils.translation import gettext as _


class FactureVenteAdmin(AdminChartMixin, admin.ModelAdmin):
    list_display = (
        "numero_de_facture",
        "type_de_facture",
        "date",
        "montant",
        "patient",
        "mode_de_reglement",
        "date_du_reglement",
        "statut_de_paiement",
        "_document_lie",
    )
    list_filter = ("type_de_facture", "mode_de_reglement", "statut_de_paiement")
    search_fields = ("numero_de_facture", "patient__nom", "patient__prenom")
    date_hierarchy = "date"
    ordering = ("-date",)

    # ChartJS config
    list_chart_type = "bar"

    def _document_lie(self, obj):
        if obj.document_lie:
            human_readable_name = obj.document_lie.name.split("/")[-1]
            return format_html(
                f'<a href="{obj.document_lie.url}">{human_readable_name}</a>'
            )
        else:
            return None

    def get_list_chart_queryset(self, changelist):
        return changelist.queryset

    def get_list_chart_data(self, queryset: "QuerySet[FactureVente]"):
        if not queryset:
            return {}

        # Get the total amount of each month
        data = (
            queryset.annotate(month=TruncMonth('date_du_reglement'))
            .values("month")
            .annotate(total=Sum("montant"))
            .order_by("month")
        )
        labels = [d["month"].strftime("%B %Y") for d in data]
        translated_labels_and_year = [
            _(label.split(" ")[0]).capitalize()
            + " "
            + label.split(" ")[1] for label in labels
        ]

        values = [d["total"] for d in data]

        return {
            "labels": translated_labels_and_year,
            "datasets": [
                {
                    "label": "Total des factures",
                    "data": values,
                    "backgroundColor": "#79aec8",
                    "borderColor": "#417690",
                    "borderWidth": 1,
                }
            ],
        }


class PrestationAdmin(admin.ModelAdmin):
    pass


admin.site.register(FactureVente, FactureVenteAdmin)
admin.site.register(Prestation, PrestationAdmin)
