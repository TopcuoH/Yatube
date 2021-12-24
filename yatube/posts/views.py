# posts/views.py
from django.http import HttpResponse
# Импортируем загрузчик.
from django.shortcuts import render


# Главная страница
def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube'
    }
    # Формируем шаблон
    return render(request, template, context)


# Страница со списком мороженого
def group_list(request):
    template = 'posts/group_list.html'
    title = 'Лев Толстой – зеркало русской революции.'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    # Формируем шаблон
    return render(request, template, context)


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    return HttpResponse(f'Пост номер {slug}')
