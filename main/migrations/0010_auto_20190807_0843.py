# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-07 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_list_produits_prix_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factures',
            name='id_c_b_f',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.CompteBancaire'),
        ),
        migrations.AlterField(
            model_name='factures',
            name='id_c_f',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Clients'),
        ),
        migrations.AlterField(
            model_name='factures',
            name='prix_t',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]