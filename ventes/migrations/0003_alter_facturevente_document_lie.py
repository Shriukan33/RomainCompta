# Generated by Django 4.1.2 on 2022-10-31 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ventes", "0002_facturevente_document_lie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facturevente",
            name="document_lie",
            field=models.FileField(
                blank=True, null=True, upload_to="documents/factures_de_ventes"
            ),
        ),
    ]
