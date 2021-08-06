from django.contrib import admin
from django.urls import path
from django.urls import re_path
from Xenon import views

urlpatterns = [
    path('', views.index),
    re_path(r'^about', views.about),
    re_path(r'^articles', views.articles),
    path('admin/', admin.site.urls),
]
