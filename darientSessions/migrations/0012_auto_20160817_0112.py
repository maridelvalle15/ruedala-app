# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('darientSessions', '0011_auto_20160816_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datoscorredor',
            name='nombre',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'Banco General', b'Banco General'), (b'Banesco', b'Banesco'), (b'Banistmo', b'Banistmo'), (b'Lafise', b'Lafise'), (b'Visa', b'Visa')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 8, 17)),
        ),
    ]
