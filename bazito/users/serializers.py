from datetime import date

from rest_framework import serializers
from users.models import LocModel, UserModel


def check_min_age(value: date):
    MIN_AGE = 9
    today = date.today()
    age = today - value
    if age.days // 365 < MIN_AGE:
        raise serializers.ValidationError(
            'Минимальный возраст регистрации – 9 лет')


class LocSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=1024)
    lat = serializers.FloatField(required=False)
    lng = serializers.FloatField(required=False)

    class Meta:
        model = LocModel
        fields = '__all__'


class UserViewSerializer(serializers.ModelSerializer):
    locations = LocSerializer(many=True)

    class Meta:
        model = UserModel
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    locations = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=LocModel.objects.all(),
        slug_field='name'
    )
    birth_date = serializers.DateField(validators=[check_min_age])

    class Meta:
        model = UserModel
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._loc = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = UserModel.objects.create(**validated_data)
        user.set_password(validated_data["password"])

        for location in self._loc:
            loc_obj, _ = LocModel.objects.get_or_create(name=location)
            user.locations.add(loc_obj)
        user.save()
        return user

    def save(self, **kwargs):
        user = super().save(**kwargs)
        if kwargs.get("password"):
            user.set_password(kwargs["password"])

        for location in self._loc:
            loc_obj, _ = LocModel.objects.get_or_create(name=location)
            user.locations.add(loc_obj)
        user.save()

        return user
