from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=60)
    student_class = models.IntegerField()
    age = models.IntegerField()

    def __repr__(self):
        return f"{self.name} (Class: {self.student_class}, Age: {self.age})"

    def __str__(self):
        return f"{self.name} (Class: {self.student_class}, Age: {self.age})"
