from django.db.models import Count, Q
from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, UpdateAPIView)
from users.models import LocModel, UserModel
from users.serializers import (LocSerializer, UserCreateSerializer,
                               UserViewSerializer)


class LocViewSet(viewsets.ModelViewSet):
    queryset = LocModel.objects.all()
    serializer_class = LocSerializer


class UsersView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserViewSerializer
    # TODO: total_ads = Count("adsmodel", filter=Q(adsmodel__is_published=True))
    # users = self.object_list.annotate(total_ads=total_ads)


class UserCreateView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserCreateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserViewSerializer
