#from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class MenuItemSerializar(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)