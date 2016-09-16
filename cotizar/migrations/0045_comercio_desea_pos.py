# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0044_auto_20160809_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='desea_pos',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'S\xc3\xad', b'S\xc3\xad'), (b'No', b'No%')]),
        ),
    ]
