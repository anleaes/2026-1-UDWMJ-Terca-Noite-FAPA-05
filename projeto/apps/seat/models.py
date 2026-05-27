from django.db import models

# Create your models here.
class Seat(models.Model):
    row = models.CharField(max_length=5)
    number = models.IntegerField()

    room = models.ForeignKey(
        'room.Room',
        on_delete=models.CASCADE,
        related_name='seats'
    )

    class Meta:
        db_table = 'seats'
        ordering = ['id']

    def __str__(self):
        return f'Seat {self.row}{self.number} (Room {self.room_id})'