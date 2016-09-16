# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0011_delete_endoso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endoso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('endoso', models.CharField(default=b'Basico', unique=True, max_length=30)),
                ('precio', models.FloatField(default=0.0)),
                ('archivo', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/cotizador_darien/static/pdf'), upload_to=b'')),
            ],
        ),
    ]
