from django import forms
from .models import *


# class AddArticleForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     image = forms.ImageField()
#     text = forms.CharField(widget=forms.Textarea({'cols': '100', 'rows': '10'}))


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['short_title']


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['short_title']
