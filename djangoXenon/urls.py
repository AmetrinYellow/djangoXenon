from django.contrib import admin
from django.urls import path
from django.urls import re_path
from Xenon import views

urlpatterns = [
    path('', views.index),
    path('add_article', views.add_article),
    re_path(r'^articles/(?P<art_short_title>.+)', views.article),
    re_path(r'^articles', views.articles),
    re_path(r'^about', views.about),
    path('admin/', admin.site.urls),
]
