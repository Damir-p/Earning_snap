# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Мужчина'),
        ('female', 'Женщина'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    photo = models.ImageField(upload_to='profile_photos/', verbose_name="Фото")
    email = models.EmailField(verbose_name="Электронная почта")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Пол")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    rating = models.FloatField(default=0.0, verbose_name="Рейтинг")
    registration_date = models.DateField(auto_now_add=True, verbose_name="Дата регистрации")

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
