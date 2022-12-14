from django.urls import path
from evishlist.views import *
app_name = 'evishlist'

urlpatterns = [
    path('', show_evishlist_ajax, name='show_evishlist_ajax'),
    path('json/', show_evishlist_json, name='show_evishlist_json'),
    path('add/', add_evishlist_ajax, name='add_evishlist_ajax'),
    path('add-flutter/', add_evishlist_flutter, name='add_evishlist_flutter'),
    path('json/<str:kategori>/', show_json_filtered, name='show_json_filtered'),
    #     path('<str:kota>/', show_evishlist_filtered,
    #          name='show_evishlist_filtered'),
]
