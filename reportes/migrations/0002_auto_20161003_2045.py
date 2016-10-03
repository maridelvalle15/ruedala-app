# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='sabe_manejar',
            field=models.CharField(max_length=2, choices=[(b'---------', b'---------'), (b'Si', b'Si'), (b'Si', b'Si'), (b'No', b'No')]),
        ),
    ]
