# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0003_auto_20161014_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carnet',
            name='fecha_entrega',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='carnet',
            name='status',
            field=models.CharField(max_length=50, choices=[(b'Sin empezar', b'Sin empezar'), (b'En proceso', b'En proceso'), (b'Listo', b'Listo'), (b'Entregado', b'Entregado')]),
        ),
    ]
