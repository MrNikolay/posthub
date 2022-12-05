from django.shortcuts import render, get_object_or_404
from .models import *

from . import cfg


# ---- Получение данных для страниц ----

class GetData:
    """Класс сбора нужных данных для функций контроллеров"""
    
    is_user_auth = cfg.is_user_auth # авторизован ли пользователь

    # Получение данных для Главной страницы
    def index_data():
        title = 'PostHub - Home'
        posts = Post.objects.all().order_by('-time_create')
        is_posts = True if len(posts) > 0 else False
        data = {
            'title': title, # Имя страницы в head -> title
            'is_user_auth': GetData.is_user_auth, # Авторизован ли пользователь
            'posts': posts, # Список всех постов -> query set
            'posts_count': len(posts), # Кол-во постов
            'is_posts': is_posts # Имеются ли вообще посты
            }

        return data

    # Получение данных для страницы добавления поста
    def addpost_data():
        title = 'PostHub - AddPost'

        data = {
            'title': title,
            'is_user_auth': GetData.is_user_auth,
        }

        return data

    # Получение данных для страницы входа
    def login_data():
        title = 'PostHub - Auth'

        data = {
            'title': title,
            'is_user_auth': GetData.is_user_auth,
        }

        return data

    # Получение данных для страницы регистрации
    def register_data():
        title = 'PostHub - Register'

        data = {
            'title': title,
            'is_user_auth': GetData.is_user_auth,
        }

        return data
    
    # Получение данных для страницы просмотра поста
    def show_post_data(post_slug):
        post = get_object_or_404(Post, slug=post_slug) # Получаем объект, либо создаём ошибку - 404 если объекта нет
        page_title = f'PostHub - {post.title}' # Заголовок страницы
        data = {
            'post': post, # ссылка на пост
            'title': page_title,
            'is_user_auth': GetData.is_user_auth,
        }

        return data

# ---- Контроллеры ----

def index(request):
    data = GetData.index_data()
    path = 'main/index.html'
    return render(request, path, context=data)


def addpost(request):
    data = GetData.addpost_data()
    path = 'main/addpost.html'
    return render(request, path, context=data)


def login(request):
    data = GetData.login_data()
    path = 'main/authorization.html'
    return render(request, path, context=data)


def register(request):
    data = GetData.register_data()
    path = 'main/registration.html'
    return render(request, path, context=data)


def show_post(request, post_slug):
    data = GetData.show_post_data(post_slug)
    path = 'main/show_post.html'
    return render(request, path, context=data)