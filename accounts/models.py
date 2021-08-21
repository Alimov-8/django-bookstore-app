from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify 

# Create your models here.


class CustomUser(AbstractUser):
    slug = models.SlugField(max_length=200, unique=True, null=True)
    phone = models.CharField(max_length=255, blank=True)
    telegram = models.URLField(blank=True)
    image = models.ImageField(upload_to='accounts/', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
