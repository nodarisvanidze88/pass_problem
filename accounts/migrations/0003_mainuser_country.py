# Generated by Django 5.0.6 on 2024-05-22 10:33

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_mainuser_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainuser',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
