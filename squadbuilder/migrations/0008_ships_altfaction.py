# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squadbuilder', '0007_expansions_wave'),
    ]

    operations = [
        migrations.AddField(
            model_name='ships',
            name='altFaction',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
    ]
