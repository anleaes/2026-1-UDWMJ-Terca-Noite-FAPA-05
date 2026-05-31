from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import PaymentEditForm
from .models import Payment
from order.models import Order


@login_required(login_url='/accounts/user_login/')
def payment_list(request):
    template_name = 'payment/payment_list.html'
    payments = Payment.objects.all()
    context = {'payments': payments}
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
            if payment.transaction_status == 'approved':
                order = payment.order
                order.status = 'paid'
                order.save()
                order.tickets.update(issued_at=timezone.now())
            return redirect('payment:payment_list')
    else:
        form = PaymentEditForm(instance=payment)

    context['form'] = form
    return render(request, template_name, context)


@login_required(login_url='/accounts/user_login/')
def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    payment.delete()
    return redirect('payment:payment_list')
