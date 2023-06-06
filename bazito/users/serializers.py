from rest_framework import serializers

from users.models import LocModel, UserModel


class LocSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = UserModel
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._loc = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = UserModel.objects.create(**validated_data)

        for location in self._loc:
            loc_obj, _ = LocModel.objects.get_or_create(name=location)
            user.locations.add(loc_obj)
        user.save()
        return user

    def save(self, **kwargs):
        user = super().save(**kwargs)

        for location in self._loc:
            loc_obj, _ = LocModel.objects.get_or_create(name=location)
            user.locations.add(loc_obj)
        user.save()

        return user
