from django.urls import path
from .views import (
    AccountDetailView,
    SignupPageView,
    AccountUpdateView,
    AccountDeleteView,
)

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),

    path('profile/<int:pk>',
         AccountDetailView.as_view(),
         name='account_detail'),

    path('profile/<int:pk>/update',
         AccountUpdateView.as_view(),
         name='account_update'),

    path('profile/<int:pk>/delete',
         AccountDeleteView.as_view(),
         name='account_delete'),
]
