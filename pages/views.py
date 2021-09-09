from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from books.models import Book
from accounts.models import CustomUser

# Create your views here.
    
def home(request):
    context = dict()
    if request.user.is_authenticated:
        books_list = Book.objects.filter(seller=request.user)
        context['books_list'] = books_list
        
    return render(request, 'home.html', context)


class AboutPageView(TemplateView):
    template_name = 'about.html'

