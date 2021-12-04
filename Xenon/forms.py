from django import forms


class AddArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    short_title = forms.CharField(max_length=20)
    image = forms.ImageField()
    text = forms.CharField(widget=forms.Textarea({'cols': '100', 'rows': '10'}))
