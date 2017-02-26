# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_preguntarespuesta_pregunta_historia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntarespuesta',
            name='pregunta',
            field=models.ForeignKey(to='paciente.Pregunta', null=True),
        ),
    ]
