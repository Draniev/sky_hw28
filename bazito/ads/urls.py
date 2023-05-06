from django.urls import path

from ads.views import page_ads


urlpatterns = [
    path('', page_ads),
]
