# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-12 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20190912_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturesedex',
            name='code_date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='code_date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='code_date',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
