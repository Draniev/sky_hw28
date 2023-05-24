from ads.views import (AdCreateView, AdDeleteView, AdDetailView,
                       AdImageUpdateView, AdsView, AdUpdateView, CatCreateView,
                       CatDeleteView, CatDetailView, CatsView, CatUpdateView)
from django.urls import path

urlpatterns = [
    path('', AdsView.as_view()),
    path('/create/', AdCreateView.as_view()),
    path('<int:pk>/', AdDetailView.as_view()),
    path('<int:pk>/update/', AdUpdateView.as_view()),
    path('<int:pk>/update/image/', AdImageUpdateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),
    path('cat/', CatsView.as_view()),
    path('cat/create/', CatCreateView.as_view()),
    path('cat/<int:pk>/', CatDetailView.as_view()),
    path('cat/<int:pk>/update/', CatUpdateView.as_view()),
    path('cat/<int:pk>/delete/', CatDeleteView.as_view()),
]
