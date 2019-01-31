# coding: utf-8
__author__ = 'annika'
__date__ = '2019-01-29 19:45'

from django.utils import timezone
from rest_framework import serializers

from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    create_time = serializers.SerializerMethodField()
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = Article
        fields = ('pk', 'title', 'author', 'read_nums', 'fav_nums', 'category',
                  'tag', 'create_time', 'category_display')

    def get_create_time(self, obj):
        time = str(obj.create_time).split('.')[0]
        create_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S").strftime('%d %m, %Y')
        return create_time
