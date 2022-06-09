from rest_framework import serializers
from .models import Restaurant, Review
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password




class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'