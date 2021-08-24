from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
    UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.db.models import Q
from django.urls import reverse_lazy

from .models import Book
from reviews.models import Review
from categories.models import Category
from cart.forms import CartAddProductForm


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
                     FormMixin,
                     DetailView):
    model = Book
    form_class = CartAddProductForm
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    # It is possible to add multiple permissions via the permission_required
    permission_required = 'books.special_status'


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


class BookUpdateView(LoginRequiredMixin,
                     UserPassesTestMixin,
                     UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    login_url = 'account_login'
    fields = [
        'category',
        'title',
        'author',
        'price',
        'cover',
        'description',
    ]

    def test_func(self):
        return self.get_object().seller == self.request.user

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.get_object().pk})


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/book_delete.html'

    def test_func(self):
        return self.get_object().seller == self.request.user

    def get_success_url(self):
        return reverse_lazy('account_detail',
                            kwargs={'slug': self.request.user.slug})


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
