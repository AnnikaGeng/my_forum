from datetime import datetime
from django.db import models

from ckeditor.fields import RichTextField

import core.models

# Create your models here.


class Article(core.models.BaseModel):
    TECH_AND_LIFE = 0
    FRONT_END = 1
    ARCHITECTURE = 2
    BLOCK_CHAIN = 3
    GAME = 4
    MOBILE = 5
    CLOUD = 6
    FUND = 7
    CATEGORY_TYPE = [
        (TECH_AND_LIFE, "程序人生"),
        (FRONT_END, "前端"),
        (ARCHITECTURE, "架构"),
        (BLOCK_CHAIN, "区块链"),
        (GAME, "游戏开发"),
        (MOBILE, "移动开发"),
        (CLOUD, "云计算"),
        (FUND, "计算机基础")
    ]
    title = models.CharField(max_length=100, verbose_name="文章标题")
    author = models.CharField(max_length=50, verbose_name="作者")
    content = RichTextField(verbose_name="内容")
    read_nums = models.IntegerField(default=0, verbose_name="阅读数")
    fav_nums = models.IntegerField(default=0, verbose_name="喜爱数")
    category = models.IntegerField(choices=CATEGORY_TYPE, default=None, verbose_name="分类")
    tag = models.CharField(max_length=100, verbose_name="标签")

    def __str__(self):
        return self.title

    class Meta(core.models.BaseMeta):
        verbose_name = "文章"
        verbose_name_plural = verbose_name