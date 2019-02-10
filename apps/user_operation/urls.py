# coding: utf-8
__author__ = 'annika'
__date__ = '2019-01-31 15:03'


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^all_comments/$', views.all_comments, name='all_comments'),
    url(r'^create_comment/$', views.create_comment, name='create_comment'),
    url(r'^latest_comments/$', views.latest_comments, name='latest_comments'),
]
urlpatterns += format_suffix_patterns(urlpatterns)