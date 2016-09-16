# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('darientSessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosEjecutivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('tlf', models.CharField(default=0, max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]*$', message=b'Este campo es num\xc3\xa9rico. Introduzca un n\xc3\xbamero')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='datoscorredor',
            name='user',
        ),
        migrations.DeleteModel(
            name='DatosCorredor',
        ),
    ]
