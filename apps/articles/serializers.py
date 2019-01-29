# coding: utf-8
__author__ = 'annika'
__date__ = '2019-01-29 19:45'

from django.utils import timezone
from rest_framework import serializers

from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('pk', 'title', 'author', 'read_nums', 'fav_nums', 'category',
                  'tag', 'create_time', 'content')