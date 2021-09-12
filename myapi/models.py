from django.db import models

class Vehicles(models.Model):
    unit = models.CharField(max_length=60)
    mileage = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    day = models.DateField()

    def __str__(self):
        return self.unit