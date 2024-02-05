from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=50, 
                             blank=False)
    body = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title
