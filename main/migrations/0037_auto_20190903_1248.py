# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-03 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20190902_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturesedex',
            name='poids_brut',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='facturesedex',
            name='poids_net',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='facturesproforma',
            name='poids_brut',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='facturesproforma',
            name='poids_net',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='facturesunpa',
            name='poids_brut',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='facturesunpa',
            name='poids_net',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='facturesunpa',
            name='prix_t',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='list_produitsedex',
            name='poids',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='list_produitsedex',
            name='prix_t',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='list_produitsproforma',
            name='poids',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='list_produitsproforma',
            name='prix_t',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='list_produitsunpa',
            name='poids',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='list_produitsunpa',
            name='prix_t',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='produits',
            name='prix_u_an',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='produits',
            name='prix_u_ar',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='produits',
            name='prix_u_fr',
            field=models.FloatField(null=True),
        ),
    ]
