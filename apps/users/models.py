# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    photo = models.ImageField(upload_to='profile_photos/', verbose_name="Фото")
    registration_date = models.DateField(auto_now_add=True, verbose_name="Дата регистрации")

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
