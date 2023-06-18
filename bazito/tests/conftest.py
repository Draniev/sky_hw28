from pytest_factoryboy import register
from tests.factories import AdsFactory, CatFactory, UserFactory


pytest_plugins = "tests.fixtures"
register(AdsFactory)
register(CatFactory)
register(UserFactory)
