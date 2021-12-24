from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Отдельная страница груп
    path('group_list/', views.group_list, name='group_list'),
    path('group/<slug:slug>/', views.group_posts),
]
