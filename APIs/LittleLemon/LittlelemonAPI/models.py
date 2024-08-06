from django.db import models


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.title

class Menuitem(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)