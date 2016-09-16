# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='gastosMedicos_accid',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='gastosMedicos_pers',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='lesiones_accidente',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='lesiones_persona',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='muerte_porAccidente',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='muerte_porPersona',
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='descuento',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='gastos_medicos',
            field=models.CharField(default=b'2,000.00/10,000.00', max_length=30, choices=[(b'500.00/2,500.00', b'500.00/2,500.00'), (b'1,000.00/5,000.00', b'1,000.00/5,000.00'), (b'2,000.00/10,000.00', b'2,000.00/10,000.00'), (b'5,000.00/25,000.00', b'5,000.00/25,000.00'), (b'10,000.00/50,000.00', b'10,000.00/50,000.00'), (b'5,000.00/35,000.00', b'5,000.00/35,000.00')]),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='impuestos',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='lesiones_corporales',
            field=models.CharField(default=b'25,000.00/50,000.00', max_length=30, choices=[(b'5,000.00/10,000.00', b'5,000.00/10,000.00'), (b'10,000.00/20,000.00', b'10,000.00/20,000.00'), (b'20,000.00/40,000.00', b'20,000.00/40,000.00'), (b'25,000.00/50,000.00', b'25,000.00/50,000.00'), (b'50,000.00/100,000.00', b'50,000.00/100,000.00'), (b'100,000.00/300,000.00', b'100,000.00/300,000.00')]),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='muerte_accidental',
            field=models.CharField(default=b'5,000.00/25,000.00', max_length=30),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='total',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='conductor',
            name='estado_civil',
            field=models.CharField(max_length=10, choices=[(b'Soltero(a)', b'Soltero(a)'), (b'Casado(a)', b'Casado(a)'), (b'Otro', b'Otro')]),
        ),
        migrations.AlterField(
            model_name='conductor',
            name='sexo',
            field=models.CharField(max_length=10, choices=[(b'Masculino', b'Masculino'), (b'Femenino', b'Femenino')]),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='colision_vuelco',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='danios_propiedad',
            field=models.CharField(default=b'50,000.00', max_length=30, choices=[(b'10,000.00', b'10,000.00'), (b'15,000.00', b'15,000.00'), (b'20,000.00', b'20,000.00'), (b'25,000.00', b'25,000.00'), (b'50,000.00', b'50,000.00'), (b'100,000.00', b'100,000.00')]),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='importacion_piezas',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='incendio_rayo',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='otros_danios',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='prima_colisionVuelco',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='prima_daniosProp',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='prima_gastosMedicos',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='prima_lesiones',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='prima_mensual',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='prima_otrosDanios',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='prima_pagoContado',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='prima_pagoVisa',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='prima_preferencialPlus',
            field=models.FloatField(default=75.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='robo_hurto',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='subtotal',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='antiguedad',
            field=models.CharField(max_length=30, choices=[(b'Menor o igual a 3 a\xc3\xb1os', b'Menor o igual a 3 a\xc3\xb1os'), (b'Mayor a 3 a\xc3\xb1os', b'Mayor a 3 a\xc3\xb1os')]),
        ),
    ]
