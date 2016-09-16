# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0039_auto_20160809_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='latitud',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='longitud',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
