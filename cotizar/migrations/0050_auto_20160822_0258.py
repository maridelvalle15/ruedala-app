# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0049_auto_20160819_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentosComercio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc', models.FileField(null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='comercio',
            name='documentos_por_enviar',
            field=models.ForeignKey(blank=True, to='cotizar.DocumentosComercio', null=True),
        ),
    ]
