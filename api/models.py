from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField(default=0)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    
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
        return str(self.user)