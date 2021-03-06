# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-29 22:18
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('order_index', models.IntegerField(default=1000)),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('content', ckeditor.fields.RichTextField(verbose_name='内容')),
                ('read_nums', models.IntegerField(default=0, verbose_name='阅读数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='喜爱数')),
                ('category', models.IntegerField(choices=[(0, '程序人生'), (1, '前端'), (2, '架构'), (3, '区块链'), (4, '游戏开发'), (5, '移动开发'), (6, '云计算'), (7, '计算机基础')], default=None, verbose_name='分类')),
                ('tag', models.CharField(max_length=100, verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ('order_index', '-create_time'),
            },
        ),
    ]
