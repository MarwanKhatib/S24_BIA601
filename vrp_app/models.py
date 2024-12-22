from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
