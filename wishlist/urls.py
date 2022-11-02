from django.urls import path
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    # path('', show_wishlist, name='show_wishlist'),
    path('', show_car, name="show_catalog"),
    path('json/', show_json_car, name="json_car"),
    # path('json2/', json_review, name="json_review"),
    path('create-ajax/', create_car_ajax, name="create_car_ajax"),
    # path('review/<int:id>', create_review, name="create_review"),
    # path('love/<int:id>', love_car, name="love_car"),
    # path('delete2/<int:id>', delete_review, name="delete_review"),
    path('delete/<int:id>', delete_car_ajax, name="delete_car_ajax"),
]
