from django.shortcuts import render, redirect, get_object_or_404

from accounts.decorators import client_required
from .forms import OrderForm
from .models import Order


@client_required
def add_order(request):
    template_name = 'order/add_order.html'
    context = {}

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('order:order_list')
    else:
        form = OrderForm()
    context['form'] = form
    return render(request, template_name, context)


@client_required
def order_list(request):
    template_name = 'order/order_list.html'
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, template_name, context)


@client_required
def edit_order(request, pk):
    template_name = 'order/edit_order.html'
    order = get_object_or_404(Order, pk=pk)
    context = {
        'order': order
    }
    return render(request, template_name, context)


@client_required
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('order:order_list')
