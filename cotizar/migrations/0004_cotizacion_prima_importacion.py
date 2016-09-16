# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0003_modelo_descuento'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='prima_importacion',
            field=models.FloatField(default=0.0),
        ),
    ]
