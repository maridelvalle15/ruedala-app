# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0004_cotizacion_prima_importacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='antiguedad',
            field=models.CharField(max_length=30),
        ),
    ]
