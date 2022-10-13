from django.urls import path
from home.views import main

app_name = 'home'

urlpatterns = [
    path('', main, name='main'),
]