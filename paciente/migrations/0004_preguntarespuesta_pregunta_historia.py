# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_auto_20170226_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntarespuesta',
            name='pregunta_historia',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
