from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Страница приложения women.')


def categories(request):
    return HttpResponse('<h1> Статьи по категориям </h1> ')
# заголовок страницы