from rest_framework import serializers
from decimal import Decimal
from .models import Menuitem, Category
import bleach
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializar(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')  
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category_id = serializers.IntegerField()
    category = CategorySerializer(read_only=True)
    
    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])
        if attrs['price'] < 2:
            raise serializers.ValidationError('Price should not be less than 2.0')
        if attrs['inventory'] < 0:
            raise serializers.ValidationError('Stock cannot be negative')
        
        #valida id de categoria
        try:
            Category.objects.get(id=attrs['category_id'])
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Invalid category ID')

        return super().validate(attrs)

    class Meta:
        model = Menuitem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
        }
    
    def calculate_tax(self, product: Menuitem):
        return product.price * Decimal(1.1)
