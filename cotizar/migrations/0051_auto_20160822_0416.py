# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0050_auto_20160822_0258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comercio',
            name='documentos_por_enviar',
        ),
        migrations.AddField(
            model_name='documentoscomercio',
            name='comercio',
            field=models.ForeignKey(blank=True, to='cotizar.Comercio', null=True),
        ),
    ]
