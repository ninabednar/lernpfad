# Generated by Django 4.1 on 2023-01-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0005_unterseite_naechste'),
    ]

    operations = [
        migrations.AddField(
            model_name='unterseite',
            name='bild',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
