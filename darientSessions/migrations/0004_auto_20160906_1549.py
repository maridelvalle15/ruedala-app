# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('darientSessions', '0003_auto_20160906_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='credito',
            name='fecha_tope',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='credito',
            name='fecha_solicitud',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
