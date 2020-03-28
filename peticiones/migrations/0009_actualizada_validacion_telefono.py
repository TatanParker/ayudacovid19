# Generated by Django 2.2.11 on 2020-03-28 17:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peticiones', '0008_cambio_verbose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peticion',
            name='telefono',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator('^(\\+34|0034|34)?[ -]*(6|7|9)[ -]*([0-9][ -]*){8}$', 'Añade un número de teléfono válido.')], verbose_name='¿Cual es tu número de teléfono?'),
        ),
        migrations.AlterField(
            model_name='solicitudaccesopeticion',
            name='telefono',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^(\\+34|0034|34)?[ -]*(6|7|9)[ -]*([0-9][ -]*){8}$', 'Añade un número de teléfono válido.')], verbose_name='¿Cual es tu número de teléfono?'),
        ),
    ]