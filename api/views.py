from django.http import JsonResponse
from .models import Restaurant
from .serializers import RestaurantSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['GET', 'POST'])
def restaurant_list(request):

    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = RestaurantSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_detail(request, id):
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'neighborhood']
    try:
        restaurant = Restaurant.objects.get(pk=id)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)