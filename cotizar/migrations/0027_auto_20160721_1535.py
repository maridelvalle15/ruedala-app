# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0026_cotizacion_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 21, 15, 35, 19, 836741, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 21, 15, 35, 27, 282592, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
