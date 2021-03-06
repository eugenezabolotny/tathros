# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0016_auto_20160220_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories'),
        ),
        migrations.AddField(
            model_name='photo',
            name='categories',
            field=models.ManyToManyField(to='proto.Category'),
        ),
        migrations.AddField(
            model_name='photographer',
            name='categories',
            field=models.ManyToManyField(to='proto.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='photographers',
            field=models.ManyToManyField(related_query_name='category', to='proto.Photographer'),
        ),
        migrations.AlterField(
            model_name='category',
            name='photos',
            field=models.ManyToManyField(related_query_name='category', to='proto.Photo'),
        ),
    ]
