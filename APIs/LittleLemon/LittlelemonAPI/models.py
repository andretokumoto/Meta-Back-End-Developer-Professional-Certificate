from django.db import models
from django.contrib.auth.models import User


'''class User_model(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(min_length=8)
    email = models.CharField(max_length=110)'''

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=200, db_index=True)
    
    def __str__(self) -> str:
        return self.title 

class Menuitem(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField(db_index=True,default=0)
    featured = models.BooleanField(db_index=True, default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(Menuitem, on_delete=models.CASCADE)
    quant = models.SmallIntegerField(),
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = ('menuitem','user')
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew  =models.ForeignKey(User,on_delete=models.SET_NULL, related_name='delivery_crew',null=True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)
    
class OrderItem(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(Menuitem, on_delete=models.CASCADE)
    quant = models.SmallIntegerField(),
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    
    class Meta:
        unique_together = ('menuitem','order')
    