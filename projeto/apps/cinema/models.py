from django.db import models

# Create your models here.
class Cinema(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20)

    class Meta:
        db_table = 'cinema'
        ordering = ['id']


    def __str__(self):
        return self.name
