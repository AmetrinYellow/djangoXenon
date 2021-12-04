from django.shortcuts import render
from django.http import HttpResponse
from djangoXenon import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *
from .helpers import *
import json
import os


def index(request):
    news_list = {"data": []}
    news = News.objects.all()[0:10]
    for one_news in news:
        data = {
            "title": one_news.title,
            "image": one_news.image,
            "text": one_news.text if len(one_news.text) < 100 else " ".join(one_news.text[:100].split(" ")[:-1]) +
                                                        f'... <a href="/news/{one_news.short_title}">читать далее</a>',
            "link": f"/news/{one_news.short_title}"
        }
        news_list["data"].append(data)
    if len(news_list["data"]) > 0:
        return render(request, "index.html", context=news_list)
    else:
        return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def add_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        short_title = create_short(request.POST.get("title"))
        image = request.FILES['image']
        text = request.POST.get("text")
        fs = FileSystemStorage()
        filename = fs.save(f"static/images/articles/{image.name}", image)
        img_url = fs.url(filename)
        add_art = Article.objects.create(title=title, short_title=short_title, image=img_url, text=text)
        return render(request, "success.html", context={"type": "article", "title": title, "link": f"/articles/{short_title}"})
    add_art_form = AddArticleForm()
    return render(request, "add_article.html", {"form": add_art_form})


def add_news(request):
    if request.method == "POST":
        title = request.POST.get("title")
        short_title = create_short(request.POST.get("title"))
        image = request.FILES['image']
        text = request.POST.get("text")
        fs = FileSystemStorage()
        filename = fs.save(f"static/images/news/{image.name}", image)
        img_url = fs.url(filename)
        add_news = News.objects.create(title=title, short_title=short_title, image=img_url, text=text)
        return render(request, "success.html", context={"type": "news", "title": title, "link": f"/news/{short_title}"})
    add_news_form = AddNewsForm()
    return render(request, "add_news.html", {"form": add_news_form})


def articles(request, page=1, count=10, max_len=100):
    art_list = {"data": []}
    arts = Article.objects.all()[count*(page-1):count*page]
    for art in arts:
        data = {
            "title": art.title,
            "image": art.image,
            "text": art.text if len(art.text) < max_len else " ".join(art.text[:max_len].split(" ")[:-1]) +
                                                        f'... <a href="/articles/{art.short_title}">читать далее</a>',
            "link": f"/news/{art.short_title}"
        }
        art_list["data"].append(data)
    return render(request, "articles.html", context=art_list)


def article(request, art_short_title):
    art = Article.objects.get(short_title=art_short_title)
    data = {
        "title": art.title,
        "image": art.image,
        "text": art.text
    }
    return render(request, "article.html", context=data)


def news(request, news_short_title):
    art = Article.objects.get(short_title=news_short_title)
    data = {
        "title": art.title,
        "image": art.image,
        "text": art.text
    }
    return render(request, "news.html", context=data)