from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from books.models import Book
from .models import CustomUser
# Create your views here.


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'account/signup.html'


class AccountDetailView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        DetailView):
    model = CustomUser
    template_name = 'account/account_detail.html'
    login_url = 'account_login'

    def test_func(self):
        obj = self.get_object()
        return obj.slug == self.request.user.slug

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.filter(seller=self.get_object())
        return context


class AccountUpdateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        UpdateView):
    model = CustomUser
    template_name = 'account/account_update.html'
    login_url = 'account_login'
    fields = ('phone', 'telegram', 'image',)

    def test_func(self):
        obj = self.get_object()
        return obj.slug == self.request.user.slug

    def get_success_url(self):
        return reverse_lazy('account_detail',
                            kwargs={'slug': self.request.user.slug})


class AccountDeleteView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        DeleteView):
    model = CustomUser
    template_name = 'account/account_delete.html'
    login_url = 'account_login'

    def get_success_url(self):
        return reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.slug == self.request.user.slug


class AccountDashboardDetailView(LoginRequiredMixin,
                                 DetailView):
    model = CustomUser
    template_name = 'account/account_dashboard.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super(AccountDashboardDetailView,
                        self).get_context_data(**kwargs)
        context['book_list'] = Book.objects.filter(seller=self.get_object(),
                                                   available=True)
        return context
