from django.urls import path
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    # path('', show_wishlist, name='show_wishlist'),
    path('', show_car, name="show_car"),
    path('', json_car, name="json_car"),
    path('', json_review, name="json_review"),
    path('', create_car, name="create_car"),
    path('', create_review, name="create_review"),
    path('', love_car, name="love_car"),
    path('', delete_review, name="delete_review"),
    path('', delete_car, name="delete_car"),

]
