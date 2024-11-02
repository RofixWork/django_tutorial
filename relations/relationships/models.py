from django.db import models


# Create your models here.
class Husband(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"


class Wife(models.Model):
    name = models.CharField(max_length=40)
    husband = models.OneToOneField(Husband, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Wife Name: {self.name}"
