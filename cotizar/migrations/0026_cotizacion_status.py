# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0025_auto_20160713_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='status',
            field=models.CharField(default=b'Enviada', max_length=30, choices=[(b'Enviada', b'Enviada'), (b'Guardada', b'Guardada'), (b'Aprobada', b'Aprobada'), (b'Rechazada', b'Rechazada')]),
        ),
    ]
