# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0002_auto_20160606_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='descuento',
            field=models.FloatField(default=1.0),
        ),
    ]
