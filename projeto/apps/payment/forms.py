from django import forms

from .models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method']


class PaymentEditForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method', 'transaction_status', 'charged_amount']
