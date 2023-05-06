from django.db import models


class CatModel(models.Model):
    name = models.CharField(max_length=50)