from django.db import models


class LocModel(models.Model):
    name = models.CharField(max_length=1024)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class UserModel(models.Model):
    ROLE = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Администратор"),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    # member, moderator, admin,
    role = models.CharField(max_length=16, choices=ROLE, default="member")
    age = models.SmallIntegerField()
    locations = models.ManyToManyField(LocModel)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
