# coding: utf-8
__author__ = 'annika'
__date__ = '2019-02-02 19:37'
import django_filters
from .models import *


class ArticleFilter(django_filters.rest_framework.FilterSet):
    """
    过滤类
    """
    title = django_filters.CharFilter(field_name='title', lookup_expr="icontains")

    class Meta:
        model = Article
        fields = ["title", "category", "tag"]