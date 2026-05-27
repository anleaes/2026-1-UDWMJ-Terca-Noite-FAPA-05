from django import forms

from .models import Payment


class PaymentCheckoutForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method', 'receipt']
        widgets = {
            'payment_method': forms.Select(
                choices=[
                    ('pix', 'PIX'),
                    ('credit_card', 'Credit card'),
                    ('debit_card', 'Debit card'),
                    ('cash', 'Cash'),
                ],
            ),
        }
