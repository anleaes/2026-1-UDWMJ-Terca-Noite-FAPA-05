from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from order.models import Order
from order.utils import orders_for_user

from .forms import PaymentCheckoutForm
from .models import Payment


@login_required(login_url='/accounts/user_login/')
def payment_list(request):
    payments = Payment.objects.select_related('order', 'order__client', 'order__user').all()
    return render(request, 'payment/payment_list.html', {'payments': payments})


@login_required(login_url='/accounts/user_login/')
def pending_payments(request):
    payments = (
        Payment.objects.filter(transaction_status=Payment.STATUS_PENDING)
        .select_related('order', 'order__client', 'order__user')
        .order_by('-created_at')
    )
    return render(request, 'payment/pending_payments.html', {'payments': payments})


@login_required(login_url='/accounts/user_login/')
def checkout(request, order_id):
    order = get_object_or_404(
        Order.objects.prefetch_related('tickets'),
        Q(pk=order_id) & orders_for_user(request.user),
    )

    if order.status != Order.STATUS_PENDING_PAYMENT:
        messages.error(request, 'This order is not ready for payment.')
        return redirect('order:order_detail', pk=order.pk)

    if not order.tickets.exists():
        messages.error(request, 'Add seats to the order before paying.')
        return redirect('ticket:select_seats', order_id=order.pk)

    if hasattr(order, 'payment'):
        messages.info(request, 'Payment already submitted for this order.')
        return redirect('order:order_detail', pk=order.pk)

    if request.method == 'POST':
        form = PaymentCheckoutForm(request.POST, request.FILES)
        if form.is_valid():
            Payment.objects.create(
                order=order,
                payment_method=form.cleaned_data['payment_method'],
                transaction_status=Payment.STATUS_PENDING,
                charged_amount=order.total_price,
                receipt=form.cleaned_data.get('receipt'),
            )
            order.status = Order.STATUS_PENDING_APPROVAL
            order.save()
            messages.success(request, 'Payment submitted. Waiting for staff approval.')
            return redirect('order:order_detail', pk=order.pk)
    else:
        form = PaymentCheckoutForm()

    return render(
        request,
        'payment/checkout.html',
        {'form': form, 'order': order},
    )


@login_required(login_url='/accounts/user_login/')
def approve_payment(request, pk):
    payment = get_object_or_404(
        Payment.objects.select_related('order').prefetch_related('order__tickets'),
        pk=pk,
    )
    order = payment.order

    if payment.transaction_status != Payment.STATUS_PENDING:
        messages.error(request, 'Only pending payments can be approved.')
        return redirect('payment:pending_payments')

    payment.transaction_status = Payment.STATUS_APPROVED
    payment.save()

    order.status = Order.STATUS_COMPLETED
    order.save()

    now = timezone.now()
    order.tickets.update(issued_at=now)

    messages.success(request, f'Payment #{payment.id} approved. Order #{order.id} completed.')
    return redirect('payment:pending_payments')


@login_required(login_url='/accounts/user_login/')
def reject_payment(request, pk):
    payment = get_object_or_404(Payment.objects.select_related('order'), pk=pk)
    order = payment.order

    if payment.transaction_status != Payment.STATUS_PENDING:
        messages.error(request, 'Only pending payments can be rejected.')
        return redirect('payment:pending_payments')

    payment.transaction_status = Payment.STATUS_REJECTED
    payment.save()

    order.tickets.all().delete()
    order.status = Order.STATUS_PENDING_SEATS
    order.total_price = 0
    order.save()

    messages.warning(request, f'Payment #{payment.id} rejected. Seats released for order #{order.id}.')
    return redirect('payment:pending_payments')
