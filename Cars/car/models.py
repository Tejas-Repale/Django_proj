from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.IntegerField()
