# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0020_auto_20160704_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='prima_mensual',
            field=models.FloatField(),
        ),
    ]
