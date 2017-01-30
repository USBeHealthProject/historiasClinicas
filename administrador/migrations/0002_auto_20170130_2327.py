# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.AddField(
            model_name='usuario',
            name='ci',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
