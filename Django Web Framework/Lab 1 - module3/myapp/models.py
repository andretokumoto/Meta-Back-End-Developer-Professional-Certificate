from django.db import models

class Drink(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
