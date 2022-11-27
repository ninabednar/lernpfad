# Generated by Django 4.1 on 2022-11-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_account_answer_option_alter_account_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='answer_option',
        ),
        migrations.AlterField(
            model_name='account',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, default=0, max_length=50),
        ),
    ]
