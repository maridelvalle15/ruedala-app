# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0021_auto_20160704_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='prima_mensual',
            field=models.FloatField(default=0.0),
        ),
    ]
