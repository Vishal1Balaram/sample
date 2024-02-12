from rest_framework import serializers
from .models import CustomerAuth

class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    class Meta:
        model = CustomerAuth
        fields = ('__all__')