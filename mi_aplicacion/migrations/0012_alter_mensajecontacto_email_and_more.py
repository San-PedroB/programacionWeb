# Generated by Django 5.0.6 on 2024-07-14 20:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0011_mensajecontacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajecontacto',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='mensajecontacto',
            name='mensaje',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mensajecontacto',
            name='telefono',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{1,15}$', message='El número de teléfono debe contener solo números y tener hasta 15 dígitos.')]),
        ),
    ]
