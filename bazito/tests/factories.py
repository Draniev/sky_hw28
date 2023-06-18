import factory
from ads.models import AdsModel, CatModel
from datetime import date
from users.models import UserModel


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel

    username = factory.Faker("name")
    password = 'qwert123'
    email = factory.Faker("email")
    birth_date = date(1970, 1, 1)
    role = 'member'


class CatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CatModel

    name = factory.Faker("word")


class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AdsModel

    name = "Тестовое объявление"
    description = factory.Faker("paragraph", nb_sentences=3)
    category = factory.SubFactory(CatFactory)
    price = 150.0
    is_published = False
    author = factory.SubFactory(UserFactory)
