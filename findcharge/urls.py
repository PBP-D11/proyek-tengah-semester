from django.urls import path
from findcharge.views import add_station, show_filtered_station, show_json, show_json_filtered, show_station

app_name = 'findcharge'

urlpatterns = [
    path('', show_station, name='show_station'),
    path('json/', show_json, name='show_json'),
    path('json/<str:kota>', show_json_filtered, name='json_filtered'),
    path('<str:kota>/', show_filtered_station, name='show_filtered_station'),
    path('add/', add_station, name='add_station'),
]