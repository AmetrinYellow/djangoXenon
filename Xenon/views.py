from django.shortcuts import render
from django.http import HttpResponse
from djangoXenon import settings
import json
import os


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def articles(request):
    articles_cat = os.path.join(settings.STATICFILES_DIRS[0], 'texts', 'articles')
    articless = {"data": []}
    for article_folder in os.listdir(articles_cat):
        with open(os.path.join(articles_cat, article_folder, "article_0.json"), "r", encoding="utf-8") as f:
            art = json.load(f, )
        with open(os.path.join(articles_cat, article_folder, art["text"]), "r", encoding="utf-8") as txt:
            text = txt.read()
        data = {
            "title": art["title"],
            "image": os.path.join("static", "texts", "articles", article_folder, art["image"]),
            "text": text
        }
        articless["data"].append(data)
    return render(request, "articles.html", context=articless)
