# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-30 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured_article',
            field=models.BooleanField(default=False, verbose_name='特色文章'),
        ),
    ]
