from django.urls import path

from categories.views import page_categories, page_cat_by_id

urlpatterns = [
    path('', page_categories, name='page_categories'),
    path('<int:pk>/', page_cat_by_id, name='page_cat_by_id'),
]