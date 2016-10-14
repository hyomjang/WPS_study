from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null = True)
    created = models.DateTimeField(auto_now_add= True)


class Car(Vehicle):
    type = models.CharField(max_length=100)

class Automobile(Vehicle):
    pass

class Buss(Vehicle):
    num_passengers = models.IntegerField()

