# coding: utf-8
__author__ = 'annika'
__date__ = '2019-01-29 19:58'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^article_list/$', views.article_list, name='article_list'),
    url(r'^article_detail/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    url(r'featured_article_list/$', views.featured_article_list, name='featured_article_list'),
    url(r'^latest_article_list/$', views.latest_article_list, name='latest_article_list')
]
urlpatterns += format_suffix_patterns(urlpatterns)