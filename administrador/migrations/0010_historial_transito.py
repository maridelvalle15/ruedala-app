# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0006_auto_20160719_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial_Transito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inferior', models.IntegerField(default=0, unique=True, choices=[(0, 0), (4, 4), (8, 8)])),
                ('superior', models.IntegerField(default=0, unique=True, choices=[(3, 3), (7, 7), (10, 10)])),
                ('factor', models.FloatField(default=0.0)),
            ],
        ),
    ]
