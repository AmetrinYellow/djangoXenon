from django.db import models


# Create your models here.
class Data(models.Model):
    pass


class Article(Data):
    short_title = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/images/articles")
    text = models.TextField()


class News(models.Model):
    short_title = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/images/articles")
    text = models.TextField()
