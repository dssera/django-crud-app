from django.contrib import admin
from django.urls import path, include
from .views import ArticleListView


urlpatterns = [
    path('', ArticleListView.as_view(template_name = 'article_list.html'), name='article-list'),
]
