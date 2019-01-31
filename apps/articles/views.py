# -*- coding: utf-8 -*-

from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework import mixins
from rest_framework import filters
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from itertools import chain

from .serializers import *
from .models import *

# Create your views here.


class ArticleView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ArticleSerializer
    filter_fields = ('category',)

    def get_queryset(self):
        return Article.objects.all()


article_list = ArticleView.as_view({'get': 'list'})
article_detail = ArticleView.as_view({'get': 'retrieve'})


class FeaturedArticleView(GenericViewSet,
                  mixins.ListModelMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ArticleSerializer
    filter_fields = ('category',)

    def get_queryset(self):
        return Article.objects.filter(featured_article=True)


featured_article_list = FeaturedArticleView.as_view({'get': 'list'})


class LatestArticleView(GenericViewSet,
                  mixins.ListModelMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ArticleSerializer
    filter_fields = ('category',)

    def get_queryset(self):
        return Article.objects.all()[:6]


latest_article_list = LatestArticleView.as_view({'get': 'list'})

