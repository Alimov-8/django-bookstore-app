import uuid
from django.contrib.auth import get_user_model
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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Book 📘'
        verbose_name_plural = 'Books 📚'


# As the project grows it might also make sense
# to split reviews off into its own dedicated app

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