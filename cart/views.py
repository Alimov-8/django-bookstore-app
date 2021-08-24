from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from books.models import Book
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request,
                  'cart/detail.html',
                  {'cart': cart})
