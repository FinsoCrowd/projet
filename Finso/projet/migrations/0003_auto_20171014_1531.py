# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-14 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0002_auto_20171014_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='id_category',
            field=models.ForeignKey(db_column='id_category', null=True, on_delete=django.db.models.deletion.CASCADE, to='projet.Categorie'),
        ),
    ]
