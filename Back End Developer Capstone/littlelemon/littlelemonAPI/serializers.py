from rest_framework import serializers
from .models import Menu
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['menu_id', 'title', 'price', 'inventory']
        
        
class UserSerializer(serializers.ModelSerializer):

     class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']