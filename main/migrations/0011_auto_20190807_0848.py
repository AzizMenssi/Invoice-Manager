# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-07 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190807_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factures',
            name='prix_t',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
