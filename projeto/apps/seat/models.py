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
        return f"Seat {self.row}{self.number} in Room {self.room.id} is {self.status}"

    def generate_seats(room):

        if room.seats.exists():
            return
        seats = []
        
        for r in range(room.rows):
            row_letter = chr(65 + r) 
            for n in range(1, room.seats_per_row + 1):
                seat = Seat(
                    row=row_letter,
                    number=n,
                    room=room
                )
                seats.append(seat)
        Seat.objects.bulk_create(seats)