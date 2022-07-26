from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=260)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now=True)
    thumb = models.ImageField(blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name='article_likes')
    dislikes = models.ManyToManyField(User,related_name='article_dislikes')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:20] + '...batafsil'

    def total_likes(self):
        return self.likes.count()
    
    def total_dislikes(self):
        return self.dislikes.count()

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.article} - {self.body}"

class About(models.Model):
    title = models.CharField(max_length=300)
    picture = models.ImageField(blank=True)
    

    def __str__(self):
        return self.title

class You(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    photo = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


