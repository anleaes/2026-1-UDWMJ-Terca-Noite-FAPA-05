from django.db import models
from genre.models import Genre
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    duration_minutes = models.IntegerField()
    age_rating = models.IntegerField()
    poster = models.ImageField(
        upload_to='movie_posters/', 
        null=True, 
        blank=True
    )
    genres = models.ManyToManyField(   
        Genre, 
        related_name='movies'
    )

    class Meta:
        db_table = 'movie'
        ordering = ['id']


    def __str__(self):
        return f"{self.title}"