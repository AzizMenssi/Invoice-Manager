# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-20 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20190819_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='adresse_an',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='clients',
            name='adresse_ar',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='clients',
            name='adresse_fr',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='clients',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='clients',
            name='nom_an',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='clients',
            name='nom_ar',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='clients',
            name='nom_fr',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='clients',
            name='numero',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
