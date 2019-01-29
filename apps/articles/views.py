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


