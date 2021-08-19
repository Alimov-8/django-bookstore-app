"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')), # swap out the built-in auth app

    # path('accounts/', include('django.contrib.auth.urls')), 
    # At this point we could further delete accounts/urls.py and accounts/views.py 
    # which were both created solely for our hand-written sign up page and are no 
    # longer being used. 

    # Local apps
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
    path('reviews/', include('reviews.urls')),
    path('categories/', include('categories.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
