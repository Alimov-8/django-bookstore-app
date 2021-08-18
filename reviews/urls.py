from django.urls import path
from .views import ReviewCreateView

urlpatterns = [
    path('<uuid:pk>/new/', ReviewCreateView.as_view(), name='review_new'),
]
