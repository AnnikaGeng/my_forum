# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-29 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.IntegerField(choices=[('TECH_AND_LIFE', '程序人生'), ('FRONT_END', '前端'), ('ARCHITECTURE', '架构'), ('BLOCK_CHAIN', '区块链'), ('GAME', '游戏开发'), ('MOBILE', '移动开发'), ('CLOUD', '云计算'), ('FUND', '计算机基础')], default=0),
        ),
    ]