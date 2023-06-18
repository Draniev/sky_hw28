import pytest


@pytest.mark.django_db
def test_ads_detail_view(client, member_token, ads_model):
    response = client.get(f'/ads/{ads_model.id}/',
                         HTTP_AUTHORIZATION=f"Bearer {member_token}")
    expected_response = {
        "id": ads_model.id,
        "category": ads_model.category.name,
        "name": ads_model.name,
        "price": ads_model.price,
        "description": ads_model.description,
        "is_published": ads_model.is_published,
        "image": None,
        "author": ads_model.author.id
    }

    assert response.status_code == 200
    print(expected_response)
    print(response.data)
    assert response.data == expected_response
