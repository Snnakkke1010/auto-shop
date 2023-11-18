from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    slug = models.SlugField(verbose_name='URL', null=True, unique=True)
    user = models.OneToOneField(User, verbose_name='Власник профіля', null=True, on_delete=models.CASCADE)
    av = models.ImageField(verbose_name='Аватарка профілю', upload_to='user-images/', null=True)

    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профіля'

    def __str__(self):
        return f'Профіль користувача - {self.user}'


