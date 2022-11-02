from django.urls import path
from news.views import show_json
from news.views import add_news, news

app_name = 'news'

urlpatterns = [
    path('', news, name='news'),
    path('json/', show_json, name='show_json'),
    path('add/', add_news, name='add_news')
]