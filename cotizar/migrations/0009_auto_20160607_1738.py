# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0008_auto_20160607_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='antiguedad',
            field=models.CharField(default=b'Menor o igual a 3 a\xc3\xb1os', max_length=30, choices=[(b'Menor o igual a 3 a\xc3\xb1os', b'Menor o igual a 3 a\xc3\xb1os'), (b'Mayor a 3 a\xc3\xb1os', b'Mayor a 3 a\xc3\xb1os')]),
        ),
    ]
