# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-16 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squadbuilder', '0006_ships_faction'),
    ]

    operations = [
        migrations.AddField(
            model_name='expansions',
            name='wave',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
