from django.urls import path
from home.views import main
from home.views import login_user
from home.views import register
from home.views import logout_user

app_name = 'home'

urlpatterns = [
    path('', main, name='main'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
]