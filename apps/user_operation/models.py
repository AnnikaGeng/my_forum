from django.db import models

import core.models
from users.models import UserProfile
from articles.models import Article
# Create your models here.


class UserLike(core.models.BaseModel):
    """
    用户点赞
    """
    user = models.ForeignKey(UserProfile, verbose_name="用户")
    article = models.ForeignKey(Article, verbose_name="文章")

    class Meta(core.models.BaseMeta):
        verbose_name = '用户点赞'
        verbose_name_plural = verbose_name
        unique_together = ("user", "article")

    def __str__(self):
        return self.user.username



