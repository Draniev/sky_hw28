from django.urls import path
from users.views import (UserCreateView, UserDeleteView, UserUpdateView,
                         UsersView)

urlpatterns = [
    path('', UsersView.as_view()),
    # path('<int:pk>/', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/update', UserUpdateView.as_view()),
    path('<int:pk>/delete', UserDeleteView.as_view()),
    # path('cat/<int:pk>/', CatDetailView.as_view())
]
