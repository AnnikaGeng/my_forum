from django.db import models

import core.models
from articles.models import Article
# Create your models here.


class Comment(core.models.BaseModel):
    """
    评论
    """
    article = models.ForeignKey(Article, verbose_name="关联文章", related_name="comments")
    name = models.CharField(max_length=100, default=None, verbose_name="姓名")
    email = models.CharField(max_length=100, default=None, verbose_name="邮箱")
    comment = models.TextField(max_length=1000, verbose_name="留言")

    class Meta(core.models.BaseMeta):
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering =('create_time',)

    def __str__(self):
        return self.name



