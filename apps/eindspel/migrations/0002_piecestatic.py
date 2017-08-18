# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eindspel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PieceStatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pieceName', models.CharField(max_length=255)),
                ('identifier', models.IntegerField()),
                ('health', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('atkRange', models.IntegerField()),
                ('movement', models.IntegerField()),
                ('abilities', models.CharField(max_length=255)),
                ('placement', models.CharField(max_length=255)),
                ('deckVal', models.IntegerField()),
                ('currentSpace', models.IntegerField()),
                ('graphic', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
