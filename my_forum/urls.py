"""my_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    # drf自带认证接口
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt认证接口
    url(r'^login/', obtain_jwt_token),
    url(r'^search/', include('haystack.urls')),
    url(r'^user_operation/', include('user_operation.urls')),
]
