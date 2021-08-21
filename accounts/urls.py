from django.urls import path
from .views import (
     AccountDetailView,
     SignupPageView,
     AccountUpdateView,
     AccountDeleteView,
     AccountDashboardDetailView,
)

urlpatterns = [
     path('signup/', SignupPageView.as_view(), name='signup'),

     path('profile/<slug:slug>',
          AccountDetailView.as_view(),
          name='account_detail'),

     path('profile/<slug:slug>/update',
          AccountUpdateView.as_view(),
          name='account_update'),

     path('profile/<slug:slug>/delete',
          AccountDeleteView.as_view(),
          name='account_delete'),

     path('<slug:slug>/',
          AccountDashboardDetailView.as_view(),
          name='account_dashboard'),
]
