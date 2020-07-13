# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-07 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190807_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factures',
            name='destination',
            field=models.CharField(blank=True, default=0, max_length=100),
            preserve_default=False,
        ),
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
            name='mode_livraison',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='factures',
            name='mode_paiement',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='factures',
            name='nb_colis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='factures',
            name='nb_conteneur',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='factures',
            name='ngp',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='factures',
            name='pays_origine',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='factures',
            name='poids_brut',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='factures',
            name='poids_net',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='factures',
            name='port_chargement',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='factures',
            name='prix_t',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]