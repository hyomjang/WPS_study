from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

class Teacher(CommonInfo):
    year = models.CharField(max_length=10)

