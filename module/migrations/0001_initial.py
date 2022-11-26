# Generated by Django 4.1 on 2022-11-26 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('nummer', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'module',
            },
        ),
        migrations.CreateModel(
            name='Frage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frage_id', models.IntegerField(default=0)),
                ('frage_titel', models.CharField(default='', max_length=200)),
                ('frage_satz', models.TextField(max_length=200)),
                ('erklaerung', models.TextField(blank=True, default='', max_length=1000)),
                ('frage_modul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module.modul')),
            ],
            options={
                'verbose_name_plural': 'fragen',
            },
        ),
        migrations.CreateModel(
            name='Antwort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antwort_id', models.IntegerField(default=0)),
                ('antwort_text', models.TextField(max_length=200)),
                ('richtige_loesung', models.BooleanField(default=False)),
                ('frage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module.frage')),
            ],
            options={
                'verbose_name_plural': 'antworten',
            },
        ),
    ]
