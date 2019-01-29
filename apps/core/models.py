from __future__ import unicode_literals
from django.db import models

# Create your models here.


class BaseManager(models.Manager):
    def get_queryset(self):
        return super(BaseManager,self).get_queryset().filter(deleted=False)

    def real_all(self):
        return super(BaseManager,self).get_queryset()


class SelectRelatedManager(BaseManager):
    def __init__(self, *related_names):
        self.related_names = related_names
        super(SelectRelatedManager, self).__init__()

    def get_queryset(self):
        return super(SelectRelatedManager, self).get_queryset().select_related(*self.related_names)


class BaseMeta:
    ordering = ('order_index', '-create_time',)


class BaseModel(models.Model):
    deleted = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    order_index = models.IntegerField(default=1000)

    objects = BaseManager()

    class Meta(BaseMeta):
        abstract = True

    def delete(self, *args, **kwargs):
        if kwargs.pop('delete', None):
            super(BaseModel, self).delete(*args, **kwargs)
        else:
            setattr(self, 'deleted', True)
            super(BaseModel, self).save(*args, **kwargs)
