# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0038_auto_20160808_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='img_front',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='comercio',
            name='img_inside',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
