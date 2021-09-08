from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

#PDF
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

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


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
    pass
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(
        response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + '/css/pdf.css')])
    return response
