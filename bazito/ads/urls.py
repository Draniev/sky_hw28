from ads.views import (AdCreateView, AdDeleteView, AdDetailView,
                       AdImageUpdateView, AdsView, AdUpdateView, CatViewSet)
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
router.register('cat', CatViewSet)

urlpatterns = [
    path('', AdsView.as_view()),
    path('create/', AdCreateView.as_view()),
    path('<int:pk>/', AdDetailView.as_view()),
    path('<int:pk>/update/', AdUpdateView.as_view()),
    path('<int:pk>/update/image/', AdImageUpdateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),
] + router.urls
