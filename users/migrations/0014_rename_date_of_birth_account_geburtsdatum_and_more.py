# Generated by Django 4.1 on 2023-01-07 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_onboarding'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='date_of_birth',
            new_name='geburtsdatum',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='picture',
            new_name='profilbild',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='phone',
            new_name='telefonnummer',
        ),
    ]
