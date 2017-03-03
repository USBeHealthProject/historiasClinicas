# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_auto_20170226_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='obligatoria',
            field=models.BooleanField(default=False),
        ),
    ]
