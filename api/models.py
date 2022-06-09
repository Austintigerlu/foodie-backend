from django.db import models

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