# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-02 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20190902_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturesedex',
            name='prix_t',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='facturesproforma',
            name='prix_t',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True),
        ),
    ]