# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0005_auto_20161003_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamos',
            name='bicipunto',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='biciescuelas',
            name='aprobado',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'Si', b'Si'), (b'No', b'No')]),
        ),
    ]
