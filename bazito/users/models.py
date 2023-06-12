from django.db import models
from django.contrib.auth.models import AbstractUser


class LocModel(models.Model):
    name = models.CharField(max_length=1024)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class UserModel(AbstractUser):
    ROLE = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Администратор"),
    ]
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # username = models.CharField(max_length=64)
    # password = models.CharField(max_length=64)
    # member, moderator, admin,
    role = models.CharField(max_length=16, choices=ROLE, default="member")
    age = models.SmallIntegerField(blank=True, null=True)
    locations = models.ManyToManyField(LocModel, blank=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
