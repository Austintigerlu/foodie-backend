from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    yelp_id = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self