from django.db import models


class Payment(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    ]

    payment_method = models.CharField(max_length=100)
    transaction_status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    charged_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    order = models.OneToOneField('order.Order', on_delete=models.CASCADE, related_name='payment')

    class Meta:
        db_table = 'payments'
        ordering = ['-id']

    def __str__(self):
        return f'Payment {self.id}'
