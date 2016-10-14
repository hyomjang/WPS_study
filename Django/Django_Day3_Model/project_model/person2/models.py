from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','XLarge'),
    )
    GENDER = (
        ('','모름'),
        ('m','남성'),
        ('f','여성')
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


