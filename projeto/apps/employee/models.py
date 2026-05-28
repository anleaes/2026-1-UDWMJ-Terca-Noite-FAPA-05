from django.db import models

from person.models import Person


class Employee(Person):
    
    hire_date = models.DateField()
    role = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'employees'
        ordering = ['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.role}'
