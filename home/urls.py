from django.urls import path
from home.views import main
from home.views import login_user
from home.views import register
from home.views import logout_user
from home.views import profile
from home.views import profile_update
from home.views import profile_json
from home.views import validate_email
from home.views import validate_phone
from home.views import validate_username

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
]