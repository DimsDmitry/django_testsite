from django.urls import path
from .views import *


urlpatterns = [
    path('', index),           #http://127.0.0.1:8000/women/
    path('cats/', categories), #http://127.0.0.1:8000/women/categories
]

#http://127.0.0.1:8000/women/ - префикс появится, потому что мы указывали его ещё в coolsite/urls.py
#Далее он будет добавляться автоматически
#если добавить сюда ещё маршрут