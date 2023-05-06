from django.urls import path

from categories.views import page_categories

urlpatterns = [
    path('', page_categories, name='page_categories'),
]