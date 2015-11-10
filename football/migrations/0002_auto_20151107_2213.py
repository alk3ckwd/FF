# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='games',
            name='humidity',
        ),
        migrations.RemoveField(
            model_name='games',
            name='temp',
        ),
        migrations.RemoveField(
            model_name='games',
            name='wind_dir',
        ),
        migrations.RemoveField(
            model_name='games',
            name='wind_speed',
        ),
    ]
