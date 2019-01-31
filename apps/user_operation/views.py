from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from .models import *
from .serializers import *
from utils.permissions import IsOwnerOrReadOnly
# Create your views here.


class UserFavViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin):
    """
    list:
        获取用户点赞列表
    retrieve:
        判断某文章是否已经点赞
    create:
        点赞
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return UserLike.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return UserLikeSerializer
        elif self.action == "create":
            return UserLikeSerializer
        return UserLikeSerializer
