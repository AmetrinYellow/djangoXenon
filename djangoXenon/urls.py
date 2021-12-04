from django.contrib import admin
from django.urls import path
from django.urls import re_path
from Xenon import views

urlpatterns = [
    path('', views.index),
    path('add_article', views.add_article),
    path('add_news', views.add_news),
    re_path(r'^edit_article/(?P<art_short_title>.+)', views.edit_article),
    re_path(r'^edit_news/(?P<news_short_title>.+)', views.edit_news),
    re_path(r'^articles/(?P<art_short_title>.+)', views.article),
    re_path(r'^articles', views.articles),
    re_path(r'^about', views.about),
    path('admin/', admin.site.urls),
    re_path(r'^news/(?P<news_short_title>.+)', views.news),
]
