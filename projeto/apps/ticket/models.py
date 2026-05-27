from django.db import models


class Ticket(models.Model):
    screening = models.ForeignKey('screening.Screening', on_delete=models.CASCADE, related_name='tickets')
    seat = models.ForeignKey('seat.Seat', on_delete=models.CASCADE, related_name='tickets')
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, related_name='tickets')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    issued_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tickets'
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=['screening', 'seat'],
                name='unique_ticket_seat_per_screening',
            ),
        ]

    def __str__(self):
        return f'{self.screening} - {self.seat}'
