# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]