# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0043_auto_20160809_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='programa_beneficios',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'Banco General', b'Banco General'), (b'Banesco', b'Banesco'), (b'Banistmo', b'Banistmo'), (b'Lafise', b'Lafise'), (b'Visa', b'Visa')]),
        ),
    ]
