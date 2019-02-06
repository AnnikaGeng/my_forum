# coding: utf-8
__author__ = 'annika'
__date__ = '2019-02-02 16:46'
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied
from datetime import datetime
import json

from utils import message

from .models import *
from .serializers import *


class LikeMixin(object):
    def add_thumbs(self, request, *args, **kwargs):
        article = request.data.get('pk', None)
        if article:
            instance = Article.objects.get(pk=article)
            instance.fav_nums += 1
            instance.save()
            response = message.success_msg()
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            response = message.failure_msg(u'没有该文章')
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
