from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone
from django.urls import reverse

class News(models.Model):
    title = models.CharField(verbose_name='Заголовок',max_length=80)
    text = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    # sex_choice = (
    #     ('М', 'Мужской'),
    #     ('Ж', 'Женский'),
    # )
    #
    # sex = models.CharField(max_length=3, choices=sex_choice)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

