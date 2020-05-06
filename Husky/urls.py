"""Husky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^djangoadmin/', admin.site.urls),
    url(r'^', include('basic.urls')),
    url(r'^', include('comments.urls')),
    url(r'^', include('chat.urls')),
    url(r'^', include('likes.urls')),
    url(r'^', include('notifications.urls')),
    url(r'^', include('userprofile.urls')),
    url(r'^', include('posts.urls')),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
