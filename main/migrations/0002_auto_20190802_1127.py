# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-02 10:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comptebancaire',
            old_name='AdresseB_an',
            new_name='adresse_b_an',
        ),
        migrations.RenameField(
            model_name='comptebancaire',
            old_name='AdresseB_ar',
            new_name='adresse_b_ar',
        ),
        migrations.RenameField(
            model_name='comptebancaire',
            old_name='AdresseB_fr',
            new_name='adresse_b_fr',
        ),
        migrations.RenameField(
            model_name='comptebancaire',
            old_name='CodeS_an',
            new_name='code_s_an',
        ),
        migrations.RenameField(
            model_name='comptebancaire',
            old_name='CodeS_ar',
            new_name='code_s_ar',
        ),
        migrations.RenameField(
            model_name='comptebancaire',
            old_name='CodeS_fr',
            new_name='code_s_fr',
        ),
        migrations.RenameField(
            model_name='comptebancaire',
            old_name='IdCB',
            new_name='id_c_b',
        ),
        migrations.RenameField(
            model_name='comptebancaire',
            old_name='NumB_an',
            new_name='num_b_an',
        ),
        migrations.RenameField(
            model_name='comptebancaire',
            old_name='NumB_ar',
            new_name='num_b_ar',
        ),
        migrations.RenameField(
            model_name='comptebancaire',
            old_name='NumB_fr',
            new_name='num_b_fr',
        ),
    ]
