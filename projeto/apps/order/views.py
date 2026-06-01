from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from ticket.models import Ticket

from .forms import OrderForm
from .models import Order


@login_required(login_url='/accounts/user_login/')
def order_list(request):
    template_name = 'order/order_list.html'
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def add_order(request):
    template_name = 'order/add_order.html'

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order:edit_order', order_id=order.id)
    else:
        form = OrderForm()

    context = {
        'form': form,
        'order': None,
        'tickets': [],
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def edit_order(request, order_id):
    template_name = 'order/add_order.html'
    order = get_object_or_404(Order, pk=order_id)
    tickets = Ticket.objects.filter(order=order)
    context = {
        'form': None,
        'order': order,
        'tickets': tickets,
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('order:order_list')
