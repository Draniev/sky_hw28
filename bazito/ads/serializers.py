from ads.models import AdsModel, CatModel
from rest_framework import serializers
from users.serializers import LocSerializer, UserViewSerializer


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatModel
        fields = '__all__'


class AdsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=False,
        slug_field='name',
        read_only=True,
    )
    # author = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='username',
    # )
    author = UserViewSerializer

    class Meta:
        model = AdsModel
        fields = '__all__'


class AdsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdsModel
        fields = ['image']


class AdsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdsModel
        exclude = ['image']
