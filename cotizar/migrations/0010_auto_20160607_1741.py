# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0009_auto_20160607_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='antiguedad',
            field=models.CharField(default=b'Menor', max_length=30, choices=[(b'Menor', b'Menor o igual a 3 a\xc3\xb1os'), (b'Mayor', b'Mayor a 3 a\xc3\xb1os')]),
        ),
    ]
