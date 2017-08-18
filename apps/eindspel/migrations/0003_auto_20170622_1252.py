# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-22 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eindspel', '0002_piecestatic'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='graphicR',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='piecestatic',
            name='graphicR',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]