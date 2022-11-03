from django.contrib import admin
from django.utils.html import format_html
from .models import FactureVente, Prestation


class FactureVenteAdmin(admin.ModelAdmin):
    list_display = ('numero_de_facture', 'type_de_facture', 'date', 'montant', 'patient', 'mode_de_reglement', 'date_du_reglement', 'statut_de_paiement', '_document_lie')
    list_filter = ('type_de_facture', 'mode_de_reglement', 'statut_de_paiement')
    search_fields = ('numero_de_facture', 'patient__nom', 'patient__prenom')
    date_hierarchy = 'date'
    ordering = ('-date',)

    def _document_lie(self, obj):
        human_readable_name = obj.document_lie.name.split('/')[-1]
        return format_html(f'<a href="{obj.document_lie.url}">{human_readable_name}</a>')

class PrestationAdmin(admin.ModelAdmin):
    pass

admin.site.register(FactureVente, FactureVenteAdmin)
admin.site.register(Prestation, PrestationAdmin)

