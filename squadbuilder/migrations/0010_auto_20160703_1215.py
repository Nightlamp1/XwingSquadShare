# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-03 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squadbuilder', '0009_upgraderestrictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upgraderestrictions',
            name='restriction',
            field=models.CharField(max_length=50),
        ),
    ]
