from django.contrib import admin

from .models import *

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'article', 'name', 'email')
    list_filter = ('article', 'name')
    search_fields = ('article',)


admin.site.register(Comment, CommentAdmin)
