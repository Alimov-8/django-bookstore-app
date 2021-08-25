import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from categories.models import Category


# Create your models here.


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    category = models.ForeignKey(Category,
                                 related_name='books',
                                 on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    class Meta:
        ordering = ('title',)
        verbose_name = 'Book'
        verbose_name_plural = 'Books 📚'
        permissions = [
            ('special_status', 'Can read all books'),
        ]
