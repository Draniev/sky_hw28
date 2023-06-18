import datetime
import pytest


@pytest.fixture()
@pytest.mark.django_db
def member_token(client, django_user_model):
    username = 'member_user'
    password = 'qwert123'
    email = 'member_user@test.ru'
    birth_date = datetime.date(1970, 1, 1)
    role = 'member'

    django_user_model.objects.create_user(
        username=username,
        password=password,
        email=email,
        birth_date=birth_date,
        role=role,
    )

    data = {"username": username, "password": password}
    response = client.post('/users/token/', data, format='json')

    return response.data['access']


@pytest.fixture()
@pytest.mark.django_db
def member_user(django_user_model):
    username = 'member_user'
    password = 'qwert123'
    email = 'member_user@test.ru'
    birth_date = datetime.date(1970, 1, 1)
    role = 'member'

    user = django_user_model.objects.create_user(
        username=username,
        password=password,
        email=email,
        birth_date=birth_date,
        role=role,
    )

    return user
