from django.urls import path
from blog.views import *
urlpatterns = [
    path('article_create/',article_create,name='article_create'),
    path('',article_func,name='article_func'),
    path('<slug>',article_post,name='article_post'),
    path('<slug>/edit',article_edit,name='article_edit'),
    path('<slug>/delete',article_delete,name='article_delete'),

    path('<slug>/like',like_article,name='article_like'),
    path('<slug>/dislikes',dislike_article,name='article_dislike'),
    path('<slug>/comment/<pk>/delete',delete_comment,name='delete-comment'),
    path('<slug>/comment/<pk>/edit',edit_comment,name="comment_edit"),
    path('about/',about,name='about'),
    path('you/',you,name='you')

]