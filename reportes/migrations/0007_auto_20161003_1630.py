# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0006_auto_20161003_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='tiempo_uso',
            field=models.CharField(max_length=3, choices=[(b'30m', b'30m'), (b'1h', b'1h'), (b'2h', b'2h'), (b'3h', b'3h')]),
        ),
    ]
