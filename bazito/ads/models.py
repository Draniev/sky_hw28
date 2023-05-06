from django.db import models


class AdsModel(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=64)
    price = models.FloatField()
    description = models.TextField()
    address = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
