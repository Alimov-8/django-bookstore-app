from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from books.models import Book
from .models import Order, OrderItem
from reviews.models import Review
from cart.cart import Cart

# Create your views here.


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'orders/order/create.html'
    fields = [
        'first_name',
        'last_name',
        'email',
        'address',
        'postal_code',
        'city'
    ]

    def form_valid(self, form):
        cart = Cart(self.request)
        self.object = form.save(commit=False)
        self.object.save()
        for item in cart:
            OrderItem.objects.create(order=self.object,
                                     book=item['book'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        # clear the cart    
        cart.clear()
        return render(self.request,
                      'orders/order/created.html',
                      self.get_context_data())
