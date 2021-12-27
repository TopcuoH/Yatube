# posts/views.py
# Импортируем загрузчик.
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Главная страница
def index(request):
    # Запрос в БД о постах,
    # Пост, сортировать(по убыванию)[10 штук]
    posts = Post.objects.order_by('-pub_date')[:10]
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    text = 'Это главная страница проекта Yatube'
    context = {
        'posts': posts,
        'title': title,
        'text': text
    }
    # Формируем шаблон
    return render(request, template, context)


# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    text = (f'Записи сообщества {slug}')
    context = {
        'text': text,
        'title': text,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
