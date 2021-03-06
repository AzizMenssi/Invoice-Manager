# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-12 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20190903_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturesedex',
            name='o_c_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesedex',
            name='o_c_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesedex',
            name='o_c_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesedex',
            name='o_t_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesedex',
            name='o_t_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesedex',
            name='o_t_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesedex',
            name='os_c_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesedex',
            name='os_c_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesedex',
            name='os_c_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesedex',
            name='os_t_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesedex',
            name='os_t_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesedex',
            name='os_t_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='o_c_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='o_c_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='o_c_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='o_t_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='o_t_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='o_t_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='os_c_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='os_c_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='os_c_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='os_t_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='os_t_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesproforma',
            name='os_t_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='o_c_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='o_c_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='o_c_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='o_t_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='o_t_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='o_t_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='os_c_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='os_c_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='os_c_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='os_t_an',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='os_t_ar',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='facturesunpa',
            name='os_t_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
