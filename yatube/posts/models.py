from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()


# Create your models here.
class Post(models.Model):
    # Текст поста Тип: TextField
    text = models.TextField()

    # Дата поста. Тип поля: DateTimeField
    # Параметр auto_now_add опраеделяет, что в поле
    # будет автоматически поставленно времяи дата созданной записи
    pub_date = models.DateTimeField(auto_now_add=True)

    # Тип ForeighKey, ссылка на модель юзера
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
        )

    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='posts'
    )
