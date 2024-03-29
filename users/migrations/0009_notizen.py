# Generated by Django 4.1 on 2022-12-29 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0003_unterseite_inhalt'),
        ('users', '0008_rename_name_account_nachname_account_vorname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notiz', models.TextField(max_length=500)),
                ('seite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module.unterseite')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
