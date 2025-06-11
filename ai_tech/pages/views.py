from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html', {'caption':"CatDjango"})

def new(request):
    return render(request, 'pages/new.html')

def data(request):
    return HttpResponse("<h1>Данные проекта</h1>"
                        "<p>На этой странице вы можете ознакомиться с основными данными вашего проекта.</p>"
                        "<p>Количество пользователей: 1234</p>"
                        "<p>Активных сессий: 89</p>"
                        "<p>Последнее обновление: 2025-04-05</p>")

def test(request):
    return HttpResponse("<h1>Тестовая страница</h1>"
                        "<p>Эта страница используется для тестирования новых функций проекта.</p>"
                        "<p>Текущий статус тестов: ✅ Все тесты пройдены</p>"
                        "<p>Время последнего тестирования: 12:45</p>"
                        "<p>Средняя скорость отклика: 230 мс</p>")
# Create your views here.
