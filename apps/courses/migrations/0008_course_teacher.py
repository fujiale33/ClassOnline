# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-01 01:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgination', '0006_auto_20180128_2110'),
        ('courses', '0007_video_learn_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgination.Teacher', verbose_name='\u8bb2\u5e08'),
        ),
    ]