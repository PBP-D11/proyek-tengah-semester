# Register your models here.
from django.contrib import admin
from .models import Topic, Post, Comment

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)