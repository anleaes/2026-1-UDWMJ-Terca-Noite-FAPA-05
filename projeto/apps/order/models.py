from django.db import models

# Create your models here.
class Order(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_PAID = 'paid'
    STATUS_CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_PAID, 'Paid'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    client = models.ForeignKey(
        'client.Client',
        on_delete=models.CASCADE,
        related_name='orders',
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'orders'
        ordering = ['id']

    def __str__(self):
        return f'Order {self.id}'
