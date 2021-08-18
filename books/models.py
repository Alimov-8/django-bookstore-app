import uuid
from django.db import models
from django.urls import reverse


# Create your models here.


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Book 📘'
        verbose_name_plural = 'Books 📚'
        permissions = [
            ('special_status', 'Can read all books'),
        ]
