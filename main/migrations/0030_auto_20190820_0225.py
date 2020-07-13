# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-20 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20190820_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='adresse_an',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='adresse_ar',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='adresse_fr',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='nom_an',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='nom_ar',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='nom_fr',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='numero',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]