# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('darientSessions', '0004_auto_20160906_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentosPersonales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc', models.FileField(null=True, upload_to=b'', blank=True)),
                ('nombre', models.CharField(default=b'', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenciasBancariass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc', models.FileField(null=True, upload_to=b'', blank=True)),
                ('nombre', models.CharField(default=b'', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenciasPersonales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc', models.FileField(null=True, upload_to=b'', blank=True)),
                ('nombre', models.CharField(default=b'', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='datossolicitante',
            name='cargo',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='datossolicitante',
            name='direccion',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='datossolicitante',
            name='identificador',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='datossolicitante',
            name='lugar_trabajo',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='datossolicitante',
            name='ocupacion',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='datossolicitante',
            name='telefono',
            field=models.CharField(default=0, max_length=100, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]*$', message=b'Este campo es num\xc3\xa9rico. Introduzca un n\xc3\xbamero')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 9, 8)),
        ),
        migrations.AddField(
            model_name='referenciaspersonales',
            name='solicitante',
            field=models.ForeignKey(blank=True, to='darientSessions.DatosSolicitante', null=True),
        ),
        migrations.AddField(
            model_name='referenciasbancariass',
            name='solicitante',
            field=models.ForeignKey(blank=True, to='darientSessions.DatosSolicitante', null=True),
        ),
        migrations.AddField(
            model_name='documentospersonales',
            name='solicitante',
            field=models.ForeignKey(blank=True, to='darientSessions.DatosSolicitante', null=True),
        ),
    ]
