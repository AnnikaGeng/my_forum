from django.contrib import admin

from .models import *

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'birthday', 'gender', 'mobile', 'email')
    search_fields = ('name', 'mobile', 'email')


class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mobile', 'code', 'create_time', 'deleted')
    list_filter = ('create_time',)
    search_fields = ('mobile',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(VerifyCode, VerifyCodeAdmin)
