from rest_framework import serializers
from .models import Restaurant
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password




class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'