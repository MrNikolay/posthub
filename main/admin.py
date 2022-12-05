from django.contrib import admin
from .models import *

# Классы отображения
class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'name', 'time_create', 'is_banned')
    list_display_links = ('login', 'name')
    search_fields = ('login', 'name')


class PostAdmin(admin.ModelAdmin):
    list_display = ('creator', 'title', 'slug', 'time_create', 'is_published')
    list_display_links = ('title', 'slug')
    search_fields = ('creator', 'title', 'short', 'slug', 'long')


admin.site.register(User, UserAdmin)

admin.site.register(Post, PostAdmin)
