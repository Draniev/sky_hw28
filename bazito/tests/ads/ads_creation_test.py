import pytest


@pytest.mark.django_db
def test_ads_creation(client, cat_model, member_token):
    data = {
        "category": cat_model.id,
        "name": "Тестовое объявление",
        "price": 150.0,
        "description": "Тестовое описание объявления",
        "is_published": False,
    }

    # print(member_user.username)
    # user_data = {"username": member_user.username, "password": 'qwert123'}
    # response = client.post('/users/token/',
    #                        data=user_data,
    #                        format='json')
    # print(response.data)
    # member_token = response.data['access']
    response = client.post('/ads/create/',
                           HTTP_AUTHORIZATION=f"Bearer {member_token}",
                           data=data,
                           format="json",
                           )

    assert response.status_code == 201
    print(response.data)
    # expected_response = {
    #     "id": ad.id,
    #     "category": ad.category.name,
    #     "name": ad.name,
    #     "price": ad.price,
    #     "description": ad.description,
    #     "is_published": ad.is_published,
    #     "image": None,
    #     "author": ad.author.id
    # }
