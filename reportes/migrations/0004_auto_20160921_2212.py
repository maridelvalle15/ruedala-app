# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0003_auto_20160921_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='biciescuelas',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='biciescuelas',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='biciescuelas',
            name='identificacion',
        ),
        migrations.RemoveField(
            model_name='biciescuelas',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='biciescuelas',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='prestamos',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='prestamos',
            name='identificacion',
        ),
        migrations.RemoveField(
            model_name='prestamos',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='prestamos',
            name='telefono',
        ),
        migrations.AddField(
            model_name='biciescuelas',
            name='usuario',
            field=models.ForeignKey(default=None, to='reportes.Usuario'),
        ),
        migrations.AddField(
            model_name='prestamos',
            name='usuario',
            field=models.ForeignKey(default=None, to='reportes.Usuario'),
        ),
    ]
