from random import randint

import factory
import pytest
from factories import AdsFactory


@pytest.mark.django_db
def test_sel_creation(client, member_token):
    data = {
        "name": factory.Faker("word"),
        "ads": []
    }

    response = client.post('/ads/sel/',
                           HTTP_AUTHORIZATION=f"Bearer {member_token}",
                           data=data,
                           format="json",
                           )

    assert response.status_code == 201
    assert len(response.data['ads']) == 0
    print(response.data)

    sel_len = randint(3, 10)
    ads = AdsFactory.create_batch(sel_len)
    ads_id_list = []
    for ad in ads:
        ads_id_list.append(ad.id)

    data = {
        "name": factory.Faker("word"),
        "ads": ads_id_list
    }

    response = client.post('/ads/sel/',
                           HTTP_AUTHORIZATION=f"Bearer {member_token}",
                           data=data,
                           format="json",
                           )

    assert response.status_code == 201
    assert len(response.data['ads']) == sel_len
