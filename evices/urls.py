from django.urls import path
from evices.views import show_evices_json, add_evices_ajax, show_evices_ajax, show_json_filtered, show_evices_filtered, add_evices_flutter

app_name = 'evices'

urlpatterns = [
    path('', show_evices_ajax, name='show_evices_ajax'),
    path('json/', show_evices_json, name='show_evices_json'),
    path('add/',add_evices_ajax, name = 'add_evices_ajax'),
    path('json/<str:kota>/', show_json_filtered, name='show_json_filtered'),
    path('add-flutter/', add_evices_flutter, name='add_evices_flutter'),
    path('<str:kota>/', show_evices_filtered, name='show_evices_filtered'),
]
