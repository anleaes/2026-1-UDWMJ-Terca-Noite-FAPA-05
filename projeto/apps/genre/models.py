from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'genre'
        ordering = ['id']

    def __str__(self):
        return self.name