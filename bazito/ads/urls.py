from django.urls import path

from ads.views import AdsView, AdDetailView, CatView, CatDetailView

urlpatterns = [
    path('', AdsView.as_view()),
    path('<int:pk>/', AdDetailView.as_view()),
    path('cat/', CatView.as_view()),
    path('cat/<int:pk>/', CatDetailView.as_view())
]
