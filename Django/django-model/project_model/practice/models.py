from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class School(models.Model):
    title = models.CharField(max_length=30)

class Major(models.Model):
    title = models.CharField(max_length=30)
