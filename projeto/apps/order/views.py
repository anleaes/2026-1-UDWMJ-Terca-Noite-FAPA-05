from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from screening.models import Screening

from .models import Order
from .utils import orders_for_user, user_owns_order


def _client_for_user(user):
    if hasattr(user, 'client_profile'):
        return user.client_profile
    return None


@login_required(login_url='/accounts/user_login/')
def order_list(request):
    orders = (
        Order.objects.filter(orders_for_user(request.user))
        .prefetch_related('tickets', 'payment', 'screening')
    )
    return render(request, 'order/order_list.html', {'orders': orders})


@login_required(login_url='/accounts/user_login/')
def start_order(request, screening_id):
    screening = get_object_or_404(Screening, pk=screening_id)
    order = Order.objects.create(
        user=request.user,
        client=_client_for_user(request.user),
        screening=screening,
        status=Order.STATUS_PENDING_SEATS,
        total_price=Decimal('0'),
    )
    return redirect('ticket:select_seats', order_id=order.pk)


@login_required(login_url='/accounts/user_login/')
def order_detail(request, pk):
    order = get_object_or_404(
        Order.objects.prefetch_related('tickets__seat', 'tickets__screening'),
        pk=pk,
    )
    is_owner = user_owns_order(request.user, order)

    return render(
        request,
        'order/order_detail.html',
        {'order': order, 'is_owner': is_owner},
    )


@login_required(login_url='/accounts/user_login/')
def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if not user_owns_order(request.user, order):
        messages.error(request, 'You can only cancel your own orders.')
        return redirect('order:order_list')

    if order.status == Order.STATUS_COMPLETED:
        messages.error(request, 'Completed orders cannot be cancelled.')
        return redirect('order:order_detail', pk=pk)

    if hasattr(order, 'payment'):
        order.payment.delete()
    order.tickets.all().delete()
    order.status = Order.STATUS_CANCELLED
    order.total_price = Decimal('0')
    order.save()
    messages.success(request, 'Order cancelled.')
    return redirect('order:order_list')
