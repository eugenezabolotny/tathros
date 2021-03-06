# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0009_auto_20160214_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='email_notification_code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_pictures'),
        ),
        migrations.AlterField(
            model_name='photographer',
            name='website',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
