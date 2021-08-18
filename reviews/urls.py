from django.urls import path
from .views import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('<uuid:pk>/new/', ReviewCreateView.as_view(), name='review_new'),
    path('<uuid:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('<uuid:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]
