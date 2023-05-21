from django.shortcuts import render
from django.http import *


# Create your views here.
def index(request):
    return HttpResponse('Страница приложения women.')


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1> Статьи по категориям </h1> <p>{catid}</p>')
# заголовок страницы


def archive(request, year):
    if int(year) > 2020:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам </h1><p>{year}</p>")


# функция будет вызываться каждый раз при исключении 404 (страница не найдена):
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
