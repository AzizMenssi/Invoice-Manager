# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-07 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20190919_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturesproforma',
            name='nb_conteneur',
            field=models.CharField(blank=True, default=0, max_length=100),
            preserve_default=False,
        ),
    ]
