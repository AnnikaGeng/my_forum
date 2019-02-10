from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from .models import *
from .serializers import *
from utils.permissions import IsOwnerOrReadOnly
# Create your views here.


class CommentViewset(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()


all_comments = CommentViewset.as_view({'get': 'list'})
create_comment = CommentViewset.as_view({'post': 'create'})


class LatestCommentViewset(GenericViewSet,
                     mixins.ListModelMixin):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()[:5]


latest_comments = LatestCommentViewset.as_view({'get': 'list'})
