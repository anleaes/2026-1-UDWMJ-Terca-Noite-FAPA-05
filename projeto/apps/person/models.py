from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table = 'person'
        ordering = ['id']


    def __str__(self):
        return f"{self.first_name} {self.last_name}"