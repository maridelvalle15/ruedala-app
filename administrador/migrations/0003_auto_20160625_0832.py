# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20160624_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sexo',
            name='sexo',
            field=models.CharField(default=b'Masculino', unique=True, max_length=20, choices=[(b'Masculino', b'Masculino'), (b'Femenino', b'Femenino')]),
        ),
    ]
