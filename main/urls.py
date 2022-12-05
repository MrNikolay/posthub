from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('addpost/', views.addpost, name='addpost'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('post/<slug:post_slug>/', views.show_post, name='show_post')
]