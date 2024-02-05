from functools import reduce
import operator
from typing import Any

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.db.models import Q

from .models import Article

class ArticleListView(generic.ListView):
    model = Article

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        # PB status means 'published'
        object_list = self.model.objects.filter(status='PB')
        if q:
            q_list = [Q(body__icontains=q), Q(author__username__icontains=q)]
            object_list = object_list.filter(reduce(operator.or_, q_list))
        return object_list
    
