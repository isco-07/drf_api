from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    first_name = models.CharField(
        max_length=100, verbose_name="Имя", help_text="Укажите Имя"
    )
    last_name = models.CharField(
        max_length=100, verbose_name="Фамилия", help_text="Укажите Фамилию"
    )
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=50, **NULLABLE, verbose_name="Телефон", help_text="Укажите телефон"
    )
    city = models.CharField(
        max_length=100, **NULLABLE, verbose_name="Город", help_text="Укажите город"
    )
    avatar = models.ImageField(
        upload_to="users/avatar",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите аватар"
    )
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
