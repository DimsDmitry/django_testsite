from django.conf.urls.static import static
from django.urls import path, re_path

from coolsite import settings
from .views import *


urlpatterns = [
    path('', index, name='home'),           #http://127.0.0.1:8000/
    path('cats/<int:catid>/', categories), #http://127.0.0.1:8000/cats/1/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]

#http://127.0.0.1:8000/women/ - префикс появится, потому что мы указывали его ещё в coolsite/urls.py
#Далее он будет добавляться автоматически
#если добавить сюда ещё маршрут
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound