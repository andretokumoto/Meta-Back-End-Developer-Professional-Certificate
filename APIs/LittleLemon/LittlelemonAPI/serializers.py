#from unittest.util import _MAX_LENGTH

'''
from rest_framework import serializers

class MenuItemSerializar(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
'''

from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

#price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']

        extra_kwargs = {
            'price': {'min_value':2},
            'stock':{'source':'inventory', 'min_value': 0},
        }
        
    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)
