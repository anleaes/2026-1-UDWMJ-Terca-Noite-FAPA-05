from django.conf import settings
from django.db import models
from person.models import Person

# Create your models here.
class Client(Person):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='client_profile',
    )
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
        return f'{self.first_name} {self.last_name}'