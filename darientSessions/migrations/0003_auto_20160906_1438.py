# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('darientSessions', '0002_auto_20160902_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('dias', models.IntegerField(default=5)),
                ('fecha_solicitud', models.DateField(default=datetime.date.today)),
                ('solicitante', models.ForeignKey(to='darientSessions.DatosSolicitante')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 9, 6)),
        ),
    ]
