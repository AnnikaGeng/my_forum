# coding: utf-8
__author__ = 'annika'
__date__ = '2019-01-31 15:02'
from datetime import datetime
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    create_time = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = fields = ('pk', 'article', 'name', 'email', 'comment', 'create_time')

    def get_create_time(self, obj):
        time = str(obj.create_time).split('.')[0]
        create_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S").strftime('%d %m, %Y')
        return create_time

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Comment.objects.create(**validated_data)
