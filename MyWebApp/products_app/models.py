from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=80)  # Set Max Characters
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()


class Time(models.Model):
    Start_Time = models.DateTimeField()
    End_Date = models.DateTimeField()
