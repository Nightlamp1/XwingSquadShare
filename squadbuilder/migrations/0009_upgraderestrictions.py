# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-03 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squadbuilder', '0008_ships_altfaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpgradeRestrictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upgrade', models.CharField(max_length=50)),
                ('restriction', models.CharField(max_length=20)),
                ('restriction_type', models.CharField(max_length=20)),
            ],
        ),
    ]
