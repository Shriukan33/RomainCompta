# Generated by Django 4.1.2 on 2022-10-31 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ventes", "0001_initial"),
        ("patients", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionpatient",
            name="facture_liee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ventes.facturevente",
            ),
        ),
    ]
