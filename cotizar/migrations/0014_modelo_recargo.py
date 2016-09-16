# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0013_auto_20160627_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo',
            name='recargo',
            field=models.FloatField(default=1.0),
        ),
    ]
