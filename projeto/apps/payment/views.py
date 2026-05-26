from django.shortcuts import render

from .forms import PaymentForm
from .models import Payment
# Create your views here.
def add_payment(request):
    template_name = 'payment/add_payment.html'
    context = {}

    if request.method == 'POST':
        form = PaymentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('payment:payment_list')
    else:
        form = PaymentForm()
    context['form'] = form
    return render(request, template_name, context)

def payment_list(request):
    template_name = 'payment/payment_list.html'
    payments = Payment.objects.all()
    context = {
        'payments': payments
    }
    return render(request, template_name, context)

def edit_payment(request, pk):
    template_name = 'payment/edit_payment.html'
    payment = get_object_or_404(Payment, pk=pk)
    context = {
        'payment': payment
    }
    return render(request, template_name, context)

def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    payment.delete()
    return redirect('payment:payment_list')