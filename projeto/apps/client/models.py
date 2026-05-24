from django.db import models
from apps.person.models import Person

# Create your models here.
class Client(Person):
    gender = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ])   
    cpf = models.CharField(max_length=11)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'client'
        ordering = ['id']

    def __str__(self):
        return self.name