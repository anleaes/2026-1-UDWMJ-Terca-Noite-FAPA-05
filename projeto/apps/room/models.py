from django.db import models

# Create your models here.
class Room(models.Model):
    capacity = models.IntegerField()
    projection_type = models.CharField(max_length=10)
    accessibility = models.BooleanField(default=False)
    cinema = models.ForeignKey('cinema.Cinema', on_delete=models.CASCADE)

    class Meta:
        db_table = 'room'
        ordering = ['id']

    def __str__(self):
        return f"Room {self.id}"
