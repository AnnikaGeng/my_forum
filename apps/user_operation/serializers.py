# coding: utf-8
__author__ = 'annika'
__date__ = '2019-01-31 15:02'
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *


class UserLikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserLike
        validators = [
            UniqueTogetherValidator(
                queryset=UserLike.objects.all(),
                fields=('user', 'article'),
                message="已经收藏"
            )
        ]
        fields = ("user", "article", "id")