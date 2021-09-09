from django.urls import path
from .views import AboutPageView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]