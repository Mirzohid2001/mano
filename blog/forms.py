from blog.models import Comment
from django import forms
from.import models

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class':'textare','size':'40'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

    class Meta:
        model = models.Article
        fields = ['title','text','slug','thumb']


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'class':'textarea','size':'40','placeholder':"o'z izohizni qoldiring..."}))

    class Meta:
        model = Comment
        fields = ['body',]

