# Generated by Django 3.2.16 on 2022-11-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_sessionpatient_facture_liee'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='compte_rendu',
            field=models.FileField(blank=True, null=True, upload_to='patients/documents/compte_rendu'),
        ),
    ]
