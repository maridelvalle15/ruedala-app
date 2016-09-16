# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cotizar.models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0022_auto_20160704_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductorvehiculo',
            name='cero_km',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='conductorvehiculo',
            name='anio',
            field=cotizar.models.PositiveSmallIntegerField(),
        ),
    ]
