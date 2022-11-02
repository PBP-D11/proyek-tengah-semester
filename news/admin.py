from django.contrib import admin

# Register your models here.

from .models import News, LinkNews

admin.site.register(News)
admin.site.register(LinkNews)