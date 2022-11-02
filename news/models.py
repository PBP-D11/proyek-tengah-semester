from django.db import models
from home.models import CustomUser
# Create your models here.
class News(models.Model):
    author = models.CharField(max_length=100,blank=True,null=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    url = models.URLField(blank=True,null=True)
    image = models.ImageField(upload_to='news_images',blank=True,null=True)

class LinkNews(models.Model):
    url = models.URLField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
