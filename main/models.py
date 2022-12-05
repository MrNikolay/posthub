from django.db import models
from django.urls import reverse

class User(models.Model):
    """Модель пользователей"""

    class Meta:
        """Настройки отображения в бд"""
        verbose_name = 'Пользователи'
        verbose_name_plural = verbose_name
        # ordering = ['-time_create', 'name']

    login = models.CharField(max_length=24, unique=True, verbose_name='Логин') # Логин пользователя по которому воспроизводится вход
    password = models.TextField(verbose_name='Пароль') # Пароль пользователя (в базе данных хранится в виде хэша sha256)
    name = models.CharField(max_length=12, unique=True, verbose_name='Ник') # Отображаемое имя пользователя
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации') # Дата и время регистрации
    is_banned = models.BooleanField(default=False, verbose_name='Бан') # Забанен ли юзер. Забаненые юзеры не могут добавлять статьи


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('user', kwargs={'user_slug': self.name})


class Post(models.Model):
    """Модель постов"""

    class Meta:
        """Настройки отображения в бд"""
        verbose_name = 'Посты'
        verbose_name_plural = verbose_name
        ordering = ['-time_create', 'title']

    creator = models.CharField(max_length=12, verbose_name='Создатель') # Имя создателя поста
    title = models.CharField(max_length=32, verbose_name='Заголовок') # Заголовок поста
    short = models.TextField(max_length=165, verbose_name='short текст') # Короткая версия поста
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') # Дата и время создния поста
    slug = models.SlugField(max_length=64, unique=True, db_index=True, verbose_name='url') # Url slug поста для собственной страницы
    long = models.TextField(max_length=1024, verbose_name='Текст поста') # Длинная версия текста поста, которая будет показана только при нажатии - "Читать пост"
    is_published = models.BooleanField(default=True, verbose_name='Опубликован') # Опубликован ли пост


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('show_post', kwargs={'post_slug': self.slug})