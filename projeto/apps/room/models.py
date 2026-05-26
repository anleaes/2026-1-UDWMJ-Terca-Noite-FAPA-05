from django.db import models
from seat.models import Seat

# Create your models here.
class Room(models.Model):
    rows = models.IntegerField(default=1)
    columns = models.IntegerField(default=1)
    projection_type = models.CharField(max_length=50)
    accessibility = models.BooleanField(default=False)
    cinema = models.ForeignKey('cinema.Cinema', on_delete=models.CASCADE, related_name='rooms')

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            self.generate_seats()

    def generate_seats(self):
        if self.seats.exists():
            return

        seats = []

        for r in range(self.rows):
            row_letter = chr(65 + r)

            for n in range(1, self.columns + 1):
                seats.append(
                    Seat(row=row_letter, number=n, room=self)
                )

        Seat.objects.bulk_create(seats)