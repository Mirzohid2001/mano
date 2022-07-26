from django.shortcuts import redirect, render

from blog.models import *
from.forms import ArticleForm, CommentForm

from django.contrib.auth.decorators import login_required

from django.db.models import Q

# Create your views here.

def article_func(request):
    articles = Article.objects.all()
    return render(request, 'article_blog.html',{'articles':articles})

def article_post(request,slug):
    article = Article.objects.get(slug=slug)
    form = CommentForm(request.POST)
    if form.is_valid() and request.method == 'POST':
            instance = form.save(commit=False)
            instance.user = request.user
            instance.article = article
            instance.save()
            return redirect('article_post',slug=slug)
    form = CommentForm
    return render(request,'article_post.html',{'article':article,'form':form})

def article_create(request):
    form = ArticleForm(request.POST or None,request.FILES)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('article_func')
    form = ArticleForm()
    return render(request, 'article_create.html',{'form':form})

def article_edit(request,slug):
    print(request.POST)
    article = Article.objects.get(slug=slug)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article_post', slug=slug)
    return render(request, 'article_edit.html',{'form':form,'article':article})

def article_delete(requset,slug):
    article = Article.objects.get(slug=slug)
    if requset.method == 'POST':
        article.delete()
        return redirect('article_func')
    return render(requset,'article_delete.html',{'article':article})

def like_article(request, slug):
    article = Article.objects.get(slug=slug)
    if request.user not in article.likes.all():
        article.likes.add(request.user)
        article.dislikes.remove(request.user)
    elif request.user in article.likes.all():
        article.likes.remove(request.user)
    return redirect('article_post',slug=slug)


def dislike_article(request,slug):
    article = Article.objects.all(slug=slug)
    
    if request.user not in article.dislike.all():
        article.dislke.add(request.user)
        article.likes.remove(request.user)
    elif request.user in article.dislike.allO():
        article.dislike.remove(request.user)
    return redirect('article_post',slug=slug)

def delete_comment(request,slug,pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('article_post',slug=slug)
    return render(request,'comment_delete.html',{'comment':comment})

def edit_comment(request,slug,pk):
    comment = Comment.objects.get(pk=pk)
    form = CommentForm(request.POST or None,instance=comment)
    if form.is_valid:
        form.save()
        return redirect('article_post',slug=slug)
    return render(request,'comment_edit.html',{"form":form,'article':comment.article})


def about(request):
    return render(request, 'about.html')


def you(request):
    yous = you.objects.get()
    form = CommentForm(request.POST)
    if form.is_valid() and request.method == 'POST':
            instance = form.save(commit=False)
            instance.user = request.user
            instance.yous = yous
            instance.save()
            return redirect('article_post',)
    form = CommentForm
    return render(request,'you.html',{ 'yous':yous,'form':form})

 



