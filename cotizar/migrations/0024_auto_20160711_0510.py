# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0023_auto_20160708_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductorvehiculo',
            name='historial_transito',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='conductorvehiculo',
            name='telefono2',
            field=models.CharField(default=b'', max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='cuota',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
