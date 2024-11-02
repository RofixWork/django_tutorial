from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=10, default="morocco")
