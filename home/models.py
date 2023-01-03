from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone
from django.urls import reverse

from users.models import Profile


class NewsQueryset(models.QuerySet):

    # def is_favorites(self):
    #     if self in Favorites.objects.filter(post=self):
    #         return True
    #     return False

    def total_count(self):
        if self.count():
            return f'Вами написано {self.count()} статьи'
        else:
            return 'Вы не успели еще написать статьи'

class News(models.Model):
    title = models.CharField(verbose_name='Заголовок',max_length=80)
    text = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    objects = NewsQueryset.as_manager()

    # sex_choice = (
    #     ('М', 'Мужской'),
    #     ('Ж', 'Женский'),
    # )
    #
    # sex = models.CharField(max_length=1, choices=sex_choice)

    # переход после добавление или обновление статьи
    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Category(models.Model):
    name = models.CharField('Категория', max_length=80, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class CommentsPostsModel(models.Model):
    text = models.TextField(verbose_name='комментарии')
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Текст : {self.text} | Автор : {self.auther}'


class Favorites(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return self.post.title

    # def is_favorites(self):
    #     pass
    # придумать метод для проверки есть ли у пользователя данный пост в избранных