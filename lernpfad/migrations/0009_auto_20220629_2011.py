# Generated by Django 3.1.7 on 2022-06-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lernpfad', '0008_patient_lernpfad_abgeschlossen'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='feedback',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='patient',
            name='fragen',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
