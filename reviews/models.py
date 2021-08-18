import uuid
from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book
from django.urls import reverse

# Create your models here.


class Review(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    book = models.ForeignKey(
            Book,
            on_delete=models.CASCADE,
            related_name='reviews',
        )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.review

    def get_absolute_url(self):
        return reverse('review_update', args=[str(self.id)])

    class Meta:
        verbose_name = 'Review 💭'
        verbose_name_plural = 'Reviews 💬'
