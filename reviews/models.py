from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book

# Create your models here.


class Review(models.Model):
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

    class Meta:
        verbose_name = 'Review 💭'
        verbose_name_plural = 'Reviews 💬'
