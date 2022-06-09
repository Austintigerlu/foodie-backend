from django.contrib import admin
from .models import Review, Restaurant

admin.site.register(Restaurant)
admin.site.register(Review)