from django.db import models
from cinema.models import Room
from movie.models import Movie

# Create your models here.

class Screening(models.Model):
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='screenings')
    room = models.ForeignKey('room.Room', on_delete=models.CASCADE, related_name='screenings')
    start_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dubbed = models.BooleanField(default=False)


    class Meta:
        db_table = 'screening'
        ordering = ['id']

    def __str__(self):
        return f"{self.movie.title} at {self.start_time}" in {self.room.cinema.name}, room{self.room.id}"