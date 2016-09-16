# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darientSessions', '0005_auto_20160908_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenciasBancarias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc', models.FileField(null=True, upload_to=b'', blank=True)),
                ('nombre', models.CharField(default=b'', max_length=100)),
                ('solicitante', models.ForeignKey(blank=True, to='darientSessions.DatosSolicitante', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='referenciasbancariass',
            name='solicitante',
        ),
        migrations.DeleteModel(
            name='ReferenciasBancariass',
        ),
    ]
