# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_medico_citas'),
        ('paciente', '0002_pregunta'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreguntaRespuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta', models.CharField(max_length=200)),
                ('historia', models.ForeignKey(to='paciente.Historia')),
            ],
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='historia',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='respuesta',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='especialidad',
            field=models.ForeignKey(to='medico.Especialidad', null=True),
        ),
        migrations.AddField(
            model_name='preguntarespuesta',
            name='pregunta',
            field=models.ForeignKey(to='paciente.Pregunta'),
        ),
    ]
