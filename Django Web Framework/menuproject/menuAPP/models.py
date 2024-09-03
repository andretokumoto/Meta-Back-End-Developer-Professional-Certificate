from django.db import models

class Menu_category(models.Model):
    menu_category_name = models.CharField(max_length=200)
    
class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.FloatField(null=False)
    category_id = models.ForeignKey(Menu_category, on_delete=models.PROTECT, default=None, related_name="category_name")
    
'''class Menuitens(models.Model):
    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    year = models.IntegerField()'''
