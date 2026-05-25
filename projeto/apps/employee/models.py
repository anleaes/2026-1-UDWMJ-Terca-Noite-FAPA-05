from django.db import models
from person.models import Person

# Create your models here.
class Employee(Person):
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'employee'
        ordering = ['id']

    def __str__(self):
        return f"{self.name} - {self.position}"