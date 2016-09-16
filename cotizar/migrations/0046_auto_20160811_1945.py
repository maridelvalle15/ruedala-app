# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0045_comercio_desea_pos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='desea_pos',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'S\xc3\xad', b'S\xc3\xad'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='disc_long',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'1-3 meses', b'1-3 meses'), (b'1-6 meses', b'1-6 meses')]),
        ),
    ]
