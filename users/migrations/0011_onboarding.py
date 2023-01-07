# Generated by Django 4.1 on 2023-01-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_notizen_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Onboarding',
            fields=[
                ('id', models.IntegerField(default=-1, primary_key=True, serialize=False)),
                ('titel', models.CharField(default='', max_length=150)),
                ('text', models.TextField(default='', max_length=1000)),
                ('has_form', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Onboarding',
            },
        ),
    ]
