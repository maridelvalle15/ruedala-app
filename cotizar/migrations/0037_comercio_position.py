# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0036_auto_20160803_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, blank=True),
        ),
    ]
