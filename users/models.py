from django.contrib.auth.models import User
from django.db import models

from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    img = models.ImageField(verbose_name='Фото', default='default_user.jpg', upload_to='users_images')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профилы'

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)