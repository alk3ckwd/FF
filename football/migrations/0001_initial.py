# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('week', models.IntegerField(default=0)),
                ('humidity', models.IntegerField(null=True, default=None, blank=True)),
                ('temp', models.IntegerField(null=True, default=None, blank=True)),
                ('condition', models.CharField(default=None, null=True, max_length=20, blank=True)),
                ('wind_speed', models.IntegerField(null=True, blank=True)),
                ('wind_dir', models.CharField(null=True, max_length=3, blank=True)),
                ('venue_type', models.CharField(null=True, max_length=100, blank=True)),
                ('venue_surface', models.CharField(null=True, max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='stats',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('team_name', models.CharField(max_length=5)),
                ('off_sl_pct', models.IntegerField(default=0)),
                ('off_sm_pct', models.IntegerField(default=0)),
                ('off_sr_pct', models.IntegerField(default=0)),
                ('off_ll_pct', models.IntegerField(default=0)),
                ('off_lm_pct', models.IntegerField(default=0)),
                ('off_lr_pct', models.IntegerField(default=0)),
                ('def_sl_pct', models.IntegerField(default=0)),
                ('def_sm_pct', models.IntegerField(default=0)),
                ('def_sr_pct', models.IntegerField(default=0)),
                ('def_ll_pct', models.IntegerField(default=0)),
                ('def_lm_pct', models.IntegerField(default=0)),
                ('def_lr_pct', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='targets',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('deep_left', models.CharField(max_length=100)),
                ('deep_middle', models.CharField(max_length=100)),
                ('deep_right', models.CharField(max_length=100)),
                ('short_left', models.CharField(max_length=100)),
                ('short_middle', models.CharField(max_length=100)),
                ('short_right', models.CharField(max_length=100)),
                ('target_team_name', models.ForeignKey(to='football.stats', related_name='target_team_name')),
            ],
        ),
        migrations.AddField(
            model_name='games',
            name='away_team',
            field=models.ForeignKey(to='football.stats', related_name='away_team'),
        ),
        migrations.AddField(
            model_name='games',
            name='home_team',
            field=models.ForeignKey(to='football.stats', related_name='home_team'),
        ),
    ]
