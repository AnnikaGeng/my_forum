# coding: utf-8
__author__ = 'annika'
__date__ = '2019-02-06 20:47'
import datetime
from haystack import indexes
from .models import *


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    author = indexes.CharField(model_attr='author')

    def get_model(self):
        return Article
