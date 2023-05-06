from django.urls import path

from ads.views import page_ads, page_ad_by_id

urlpatterns = [
    path('', page_ads),
    path('<int:pk>/', page_ad_by_id),
]
