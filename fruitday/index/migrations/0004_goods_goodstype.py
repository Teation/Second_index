# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-01 02:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goodsType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.GoodsType'),
        ),
    ]
