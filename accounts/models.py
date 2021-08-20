from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField, URLField

# Create your models here.


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=255, blank=True)
    telegram = models.URLField(blank=True)
    image = models.ImageField(upload_to='accounts/', blank=True)
