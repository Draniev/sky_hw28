from django.urls import path

from ads.views import AdsView, AdDetailView

urlpatterns = [
    path('', AdsView.as_view()),
    path('<int:pk>/', AdDetailView.as_view()),
]
