from django.urls import path
from home.views import *

app_name = 'home'

urlpatterns = [
    path('', main, name='main'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='user-profile'), 
    path('profile-update/', profile_update, name='profile-update'),
    path('json/', profile_json, name='profile-json'),
    path('validate-username/', validate_username, name='validate-username'),
    path('validate-email/', validate_email, name='validate-email'),
    path('validate-phone/', validate_phone, name='validate-phone'),
    path('login-flutter/', login_user_flutter, name='login-flutter'),
    path('register-flutter/', register_flutter, name='register-flutter'),
    path('logout-flutter/',logout_user_flutter, name='logout-flutter'),
]