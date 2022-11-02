from django.db import models
from home.models import CustomUser
# Create your models here.
class News(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='news_images')

class LinkNews(models.Model):
    url = models.URLField()
