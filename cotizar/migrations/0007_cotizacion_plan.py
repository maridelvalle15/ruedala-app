# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0006_conductor_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='plan',
            field=models.CharField(default=b'B\xc3\xa1sico', max_length=10),
        ),
    ]
