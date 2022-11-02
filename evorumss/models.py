from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from home.models import CustomUser
# Create your models here.

class Topic(models.Model):
    """ Topics contain posts """

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('evorumss:topic-detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title

class Post(models.Model):
    """ Posts can be found under its topic. """

    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50, default='untitled')
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('evorumss:post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    """ Comments are replies to posts """

    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    def __str__(self):
        return self.body
