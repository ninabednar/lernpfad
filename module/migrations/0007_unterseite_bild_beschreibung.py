# Generated by Django 4.1 on 2023-01-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0006_unterseite_bild'),
    ]

    operations = [
        migrations.AddField(
            model_name='unterseite',
            name='bild_beschreibung',
            field=models.TextField(default='', max_length=200),
        ),
    ]