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
        null=True,
        related_name='news',
    )
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст новости')
    likes = models.ManyToManyField(
        Users,
        verbose_name='Понравилось пользователям',
        blank=True,
        related_name='likes'
    )
    dc = models.DateTimeField('Дата новости', auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    @property
    def likes_count(self) -> int:
        return self.likes.count()

    @property
    def comments_count(self) -> int:
        return self.comments.count()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-dc',)


class Comments(models.Model):
    author = models.ForeignKey(
        Users,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    news = models.ForeignKey(
        News,
        verbose_name='Новость',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.CharField('Текст комментария', max_length=255)
    dc = models.DateTimeField('Дата комментария', auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.author}-{self.text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-dc',)
