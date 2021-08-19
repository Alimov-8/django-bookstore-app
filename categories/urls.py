from django.urls import path
from .views import BookByCategoryListView

urlpatterns = [
    path('<slug:category_slug>/',
         BookByCategoryListView.as_view(),
         name='book_list_by_category'),
]
