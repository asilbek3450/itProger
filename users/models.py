from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):

    first_name = models.CharField(max_length=50, verbose_name='Ism')
    last_name = models.CharField(max_length=50, verbose_name='Familiya')

    username = models.CharField(max_length=50, verbose_name='Foydalanuvchi nomi', unique=True)
    email = models.EmailField(max_length=50, verbose_name='Email')

    password1 = models.CharField(max_length=50, verbose_name='Parol')
    password2 = models.CharField(max_length=50, verbose_name='Parolni takrorlang')

    image = models.ImageField(upload_to='users_images/', null=True, blank=True, verbose_name='Profil rasmi')

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return self.username
