# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-18 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20190818_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factures',
            name='poids_brut',
            field=models.DecimalField(decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='factures',
            name='poids_net',
            field=models.DecimalField(decimal_places=3, max_digits=20),
        ),
        migrations.AlterField(
            model_name='list_produits',
            name='poids',
            field=models.DecimalField(decimal_places=3, max_digits=20),
        ),
    ]