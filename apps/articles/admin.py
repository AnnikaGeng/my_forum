from django.contrib import admin

from .models import *

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'read_nums', 'fav_nums', 'category', 'tag', 'create_time', 'deleted')
    list_filter = ('create_time', 'author', 'category', 'tag')
    search_fields = ('title', 'author', 'category', 'tag')


admin.site.register(Article, ArticleAdmin)
