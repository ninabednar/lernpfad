# Generated by Django 3.1.7 on 2022-07-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lernpfad', '0015_auto_20220706_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antwort',
            name='erklaerung',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
