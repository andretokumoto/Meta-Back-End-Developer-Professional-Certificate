from django.db import models

class Menuitens(models.Model):
    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    year = models.IntegerField()
