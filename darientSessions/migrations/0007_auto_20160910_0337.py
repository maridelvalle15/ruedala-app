# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('darientSessions', '0006_auto_20160908_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='credito',
            name='status',
            field=models.CharField(default=b'Recibido', max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 9, 10)),
        ),
    ]
