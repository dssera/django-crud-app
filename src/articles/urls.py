from django.contrib import admin
from django.urls import path, include
from .views import ArticleListView, ArticleDetailView


urlpatterns = [
    path('', ArticleListView.as_view(template_name='article_list.html'), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
