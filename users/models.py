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
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefon raqam')
    address = models.CharField(max_length=128, null=True, blank=True, verbose_name='Manzil')

    website = models.URLField(max_length=128, null=True, blank=True, verbose_name='Veb-sayt')
    github = models.URLField(max_length=128, null=True, blank=True, verbose_name='Github')
    twitter = models.URLField(max_length=128, null=True, blank=True, verbose_name='Twitter')
    instagram = models.URLField(max_length=128, null=True, blank=True, verbose_name='Instagram')
    facebook = models.URLField(max_length=128, null=True, blank=True, verbose_name='Facebook')

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def save(self, *args, **kwargs):
        if self.phone_number:
            self.phone_number = self.phone_number.replace(' ', '')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

