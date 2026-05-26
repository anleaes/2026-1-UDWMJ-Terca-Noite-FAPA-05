from django.conf import settings
from django.db import models

from person.models import Person


class Employee(Person):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='employee_profile',
    )
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'employee'
        ordering = ['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.position}'
