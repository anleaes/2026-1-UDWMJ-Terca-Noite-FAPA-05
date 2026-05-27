from django.conf import settings
from django.db import models


class Order(models.Model):
    STATUS_PENDING_SEATS = 'pending_seats'
    STATUS_PENDING_PAYMENT = 'pending_payment'
    STATUS_PENDING_APPROVAL = 'pending_approval'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELLED = 'cancelled'

    STATUS_CHOICES = [
        (STATUS_PENDING_SEATS, 'Pending seats'),
        (STATUS_PENDING_PAYMENT, 'Pending payment'),
        (STATUS_PENDING_APPROVAL, 'Pending approval'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=STATUS_PENDING_SEATS)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        null=True,
        blank=True,
    )
    client = models.ForeignKey(
        'client.Client',
        on_delete=models.CASCADE,
        related_name='orders',
        null=True,
        blank=True,
    )
    screening = models.ForeignKey(
        'screening.Screening',
        on_delete=models.CASCADE,
        related_name='orders',
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'orders'
        ordering = ['-id']

    def __str__(self):
        return f'Order {self.id}'
