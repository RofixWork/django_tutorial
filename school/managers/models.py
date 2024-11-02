from django.db import models

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    hire_date = models.DateField()
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)