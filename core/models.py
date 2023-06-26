from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

DjangoUser = get_user_model()


class Users(DjangoUser):
    class Meta:
        proxy = True


class News(models.Model):
    author = models.ForeignKey(
        Users,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст новости')
    dc = models.DateTimeField('Дата новости', auto_now_add=True)


class Comments(models.Model):
    author = models.ForeignKey(
        Users,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    news = models.ForeignKey(
        News,
        verbose_name='Новость',
        on_delete=models.CASCADE,
    )
    text = models.CharField('Текст комментария', max_length=255)
    dc = models.DateTimeField('Дата комментария', auto_now_add=True)
