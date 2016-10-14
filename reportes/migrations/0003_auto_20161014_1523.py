# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0002_carnet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carnet',
            name='status',
            field=models.CharField(max_length=50, choices=[(b'No se ha empezado', b'No se ha empezado'), (b'En proceso', b'En proceso'), (b'Listo', b'Listo'), (b'Entregado', b'Entregado')]),
        ),
    ]
