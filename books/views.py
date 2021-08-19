from categories.models import Category
from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Book
from reviews.models import Review
from django.db.models import Q
from django.urls import reverse_lazy


# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.filter(available=True)
        categories = Category.objects.all()
        context['book_list'] = books
        context['categories'] = categories
        return context


class BookDetailView(LoginRequiredMixin,
                     # PermissionRequiredMixin,
                     DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    # It is possible to add multiple permissions via the permission_required
    permission_required = 'books.special_status'


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'books/book_new.html'
    fields = [
        'category',
        'title',
        'author',
        'price',
        'cover',
        'description',
    ]

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_list')
