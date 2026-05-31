from django.db import models


class Payment(models.Model):
    PAYMENT_METHOD_PIX = 'pix'
    PAYMENT_METHOD_CREDIT_CARD = 'credit_card'
    PAYMENT_METHOD_DEBIT_CARD = 'debit_card'
    PAYMENT_METHOD_CHOICES = [
        (PAYMENT_METHOD_PIX, 'PIX'),
        (PAYMENT_METHOD_CREDIT_CARD, 'Credit Card'),
        (PAYMENT_METHOD_DEBIT_CARD, 'Debit Card'),
    ]

    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    ]

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
    )
    transaction_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    charged_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.OneToOneField(
        'order.Order',
        on_delete=models.CASCADE,
        related_name='payment',
    )

    class Meta:
        db_table = 'payments'
        ordering = ['id']

    def __str__(self):
        return f'Payment {self.id}'
