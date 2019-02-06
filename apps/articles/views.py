# -*- coding: utf-8 -*-

from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from itertools import chain

from .serializers import *
from .models import *
from .mixins import *
from .filters import *

# Create your views here.


class ArticlePagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 100


class ArticleView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    filter_class = ArticleFilter
    search_fields = ('title', 'tag', 'content')

    def get_queryset(self):
        return Article.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.read_nums += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


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


class LikeViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                  mixins.ListModelMixin, mixins.RetrieveModelMixin, LikeMixin):
    permission_classes = (AllowAny,)
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()


add_thumbs = LikeViewSet.as_view({'post': 'add_thumbs'})




