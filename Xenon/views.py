from django.shortcuts import render
from django.http import HttpResponse
from djangoXenon import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *
import json
import os


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def add_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        short_title = request.POST.get("short_title")
        image = request.FILES['image']
        text = request.POST.get("text")
        fs = FileSystemStorage()
        filename = fs.save(f"static/images/articles/{image.name}", image)
        img_url = fs.url(filename)
        add_art = Article.objects.create(title=title, short_title=short_title, image=img_url, text=text)
        return render(request, "success.html", context={"art_title": title, "art_link": f"/articles/{short_title}"})
    add_art_form = AddArticleForm()
    return render(request, "add_article.html", {"form": add_art_form})


def articles(request, page=1, count=10, max_len=100):
    art_list = {"data": []}
    arts = Article.objects.all()[count*(page-1):count*page]
    for art in arts:
        data = {
            "title": art.title,
            "image": art.image,
            "text": art.text if len(art.text) < max_len else " ".join(art.text[:max_len].split(" ")[:-1]) +
                                                        f'... <a href="/articles/{art.short_title}">читать далее</>'
        }
        art_list["data"].append(data)
    return render(request, "articles.html", context=art_list)


def article(request, art_short_title):
    # article_cat = os.path.join(settings.STATICFILES_DIRS[0], 'texts', 'articles', article_id)
    # with open(os.path.join(article_cat, "article.json"), "r", encoding="utf-8") as f:
    #     art = json.load(f)
    # with open(os.path.join(article_cat, art["text"]), "r", encoding="utf-8") as txt:
    #     text = txt.read()
    # data = {
    #     "title": art["title"],
    #     "image": os.path.join("static", "texts", "articles", article_id, art["image"]),
    #     "text": text
    # }
    # return render(request, "article.html", context=data)
    art = Article.objects.get(short_title=art_short_title)
    data = {
        "title": art.title,
        "image": art.image,
        "text": art.text
    }
    return render(request, "article.html", context=data)
