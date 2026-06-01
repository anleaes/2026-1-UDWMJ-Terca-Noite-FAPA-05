from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from order.models import Order

from .forms import PaymentEditForm, PaymentForm
from .models import Payment


@login_required(login_url='/accounts/user_login/')
def payment_list(request):
    template_name = 'payment/payment_list.html'
    payments = Payment.objects.all()
    context = {'payments': payments}
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def add_payment(request, order_id):
    template_name = 'payment/add_payment.html'
    order = get_object_or_404(Order, pk=order_id)

    if hasattr(order, 'payment'):
        return redirect('order:edit_order', order_id=order.id)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.order = order
            payment.transaction_status = Payment.STATUS_PENDING
            payment.charged_amount = order.total_price
            payment.save()
            return redirect('order:edit_order', order_id=order.id)
    else:
        form = PaymentForm()

    context = {
        'form': form,
        'order': order,
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def edit_payment(request, pk):
    template_name = 'payment/edit_payment.html'
    payment = get_object_or_404(Payment, pk=pk)
    context = {}

    if request.method == 'POST':
        form = PaymentEditForm(request.POST, instance=payment)
        if form.is_valid():
            payment = form.save()
            if payment.transaction_status == Payment.STATUS_APPROVED:
                order = payment.order
                order.status = Order.STATUS_PAID
                order.save()
                order.tickets.update(issued_at=timezone.now())
            return redirect('payment:payment_list')
    else:
        form = PaymentEditForm(instance=payment)

    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def delete_payment(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if hasattr(order, 'payment'):
        order.payment.delete()
    return redirect('order:edit_order', order_id=order_id)
