from django.db import models
from django.urls import reverse

class User(models.Model):
    """Модель пользователей"""
    login = models.CharField(max_length=24, unique=True) # Логин пользователя по которому воспроизводится вход
    password = models.TextField() # Пароль пользователя (в базе данных хранится в виде хэша sha256)
    name = models.CharField(max_length=12, unique=True) # Отображаемое имя пользователя
    time_create = models.DateTimeField(auto_now_add=True) # Дата и время регистрации
    is_banned = models.BooleanField(default=False) # Забанен ли юзер. Забаненые юзеры не могут добавлять статьи


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('user', kwargs={'user_slug': self.name})


class Post(models.Model):
    """Модель постов"""
    creator = models.CharField(max_length=12) # Имя создателя поста
    title = models.CharField(max_length=32) # Заголовок поста
    short = models.TextField(max_length=165) # Короткая версия поста
    time_create = models.DateTimeField(auto_now_add=True) # Дата и время создния поста
    slug = models.SlugField(max_length=64, unique=True, db_index=True) # Url slug поста для собственной страницы
    long = models.TextField(max_length=1024) # Длинная версия текста поста, которая будет показана только при нажатии - "Читать пост"
    is_published = models.BooleanField(default=True) # Опубликован ли пост


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('show_post', kwargs={'post_slug': self.slug})