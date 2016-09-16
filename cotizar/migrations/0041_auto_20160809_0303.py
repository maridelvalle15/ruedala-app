# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cotizar.models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0040_auto_20160809_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercio',
            name='img_front',
            field=models.FileField(null=True, upload_to=cotizar.models.generate_filename_front, blank=True),
        ),
        migrations.AlterField(
            model_name='comercio',
            name='img_inside',
            field=models.FileField(null=True, upload_to=cotizar.models.generate_filename_in, blank=True),
        ),
    ]
