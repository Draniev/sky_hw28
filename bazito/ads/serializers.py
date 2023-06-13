from ads.models import AdsModel, CatModel, SelModel
from rest_framework import serializers
from users.models import UserModel
from users.serializers import UserViewSerializer


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


class SelCreateSerializer(serializers.ModelSerializer):
    # owner = UserViewSerializer
    # ads = AdsSerializer(many=True)
    owner = serializers.SlugRelatedField(
        required=False,
        queryset=UserModel.objects.all(),
        slug_field='username',
    )
    ads = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=AdsModel.objects.all(),
        slug_field='id',
    )

    # def is_valid(self, raise_exception=False):
    #     # self.initial_data['owner'] = request.user.username
    #     return super().is_valid(raise_exception=raise_exception)

    class Meta:
        model = SelModel
        fields = '__all__'


class SelViewSerializer(serializers.ModelSerializer):
    # owner = UserViewSerializer
    ads = AdsSerializer(many=True)
    owner = serializers.SlugRelatedField(
        required=False,
        queryset=UserModel.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = SelModel
        fields = '__all__'
