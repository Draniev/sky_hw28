from django.urls import path
from users.views import (UserCreateView, UserDeleteView, UserUpdateView,
                         UsersView, LocViewSet)
from rest_framework import routers

router = routers.SimpleRouter()
router.register('loc', LocViewSet)

urlpatterns = [
    path('', UsersView.as_view()),
    # path('<int:pk>/', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    # path('cat/<int:pk>/', CatDetailView.as_view())
]

urlpatterns += router.urls
