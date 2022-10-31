from django.urls import path
from home.views import main
from home.views import login_user
from home.views import register
from home.views import logout_user
from home.views import profile
from home.views import profile_update
from home.views import profile_json

app_name = 'home'

urlpatterns = [
    path('', main, name='main'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='user-profile'), 
    path('profile-update/', profile_update, name='profile-update'),
    path('json/', profile_json, name='profile-json'),
]