from django.db import models

# Create your models here.
class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, related_name='orders')

    class Meta:
        db_table = 'orders'
        ordering = ['id']

    def __str__(self):
        return f"Order {self.id}"