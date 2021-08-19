from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from books.models import Book
from .models import Category

# Create your views here.


class BookByCategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'book_list'
    template_name = 'books/book_list_by_category.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.filter(slug=self.kwargs['category_slug']).first()
        books = Book.objects.filter(category=category.id)
        context['book_list'] = books
        context['category'] = category
        return context

