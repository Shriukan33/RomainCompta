# Generated by Django 3.2.16 on 2022-11-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_patient_compte_rendu'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='suivi',
            field=models.CharField(choices=[('Y', 'En cours'), ('N', 'Terminé')], default='Y', max_length=1),
        ),
    ]
