from django.db import models

# Create your models here.

class Measurement(models.Model):
    location  = models.CharField(max_length=200)
    UserName  = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField( max_digits=10, decimal_places=2)
    created = models.DateField( auto_now_add=True)

def __str__(self):
    return f"distance from the {self.location} and {self.destination} is {self.distance} km"