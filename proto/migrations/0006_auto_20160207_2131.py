# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 21:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0005_auto_20160207_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='geo',
            new_name='point',
        ),
    ]
