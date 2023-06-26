from django.contrib import admin

from core import models


@admin.register(models.News)
class News(admin.ModelAdmin):
    list_display = ('title', 'author', 'dc', 'comments_count', 'likes_count')
    search_fields = ('title', 'author')
    search_help_text = 'Поиску по заголовку или автору'


@admin.register(models.Comments)
class Comments(admin.ModelAdmin):
    list_display = ('text', 'author', 'news', 'dc')
    search_fields = ('author', 'news')
    search_help_text = 'Поиску по новости или автору'
