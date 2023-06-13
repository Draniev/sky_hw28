from django.db import models
from users.models import UserModel


class CatModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категори'


class AdsModel(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='ads_images/')
    category = models.ForeignKey(CatModel, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class SelModel(models.Model):
    name = models.CharField(max_length=255, default='favorites')
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    ads = models.ManyToManyField(AdsModel, blank=True)

    def __str__(self) -> str:
        return f"{self.owner.username} – {self.name}"

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'
