from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from books.models import Book
from reviews.models import Review
from django.urls import reverse_lazy

# Create your views here.


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'reviews/review_new.html'
    fields = ('review',)

    def form_valid(self, form):
        form.instance.book_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        context['book'] = Book.objects.filter(pk=self.kwargs['pk']).first()
        return context

