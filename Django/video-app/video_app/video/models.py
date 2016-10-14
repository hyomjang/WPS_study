from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Video(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    description = models.TextField()
    youtube_urls = models.CharField(max_length=100)
    youtube_views = models.IntegerField(default=0)
    youtube_likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title