import pytest
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_ads_list_view(client, member_token):
    ads = AdsFactory.create_batch(10)
    response = client.get('/ads/',
                         HTTP_AUTHORIZATION=f"Bearer {member_token}")

    assert response.status_code == 200
    print(response.data)
    assert len(response.data) == len(ads)
    i = 0
    for ad in ads:
        expected_response = {
            "id": ad.id,
            "category": ad.category.name,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": None,
            "author": ad.author.id
        }
        assert expected_response == response.data[i]
        i += 1
