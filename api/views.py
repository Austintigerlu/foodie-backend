from os import stat
from django.http import JsonResponse
from .models import Restaurant, Review
from .serializers import RestaurantSerializer, ReviewSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['GET'])
def restaurant_list(request):

    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_detail(request, pk):
    
    try:
        restaurant = Restaurant.objects.get(id=pk)
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createRestaurantReview(request, pk):
    user = request.user
    restaurant = Restaurant.objects.get(id=pk)
    data = request.data
    print(user)
    alreadyExists = restaurant.review_set.filter(user=user).exists()
    if alreadyExists:
        content = {'details': 'You have already reviewed this restaurant'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    elif data['rating'] == 0:
        content = {'details': 'Please select rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    else:
        review = Review.objects.create(
            user=user,
            restaurant=restaurant,
            rating= data['rating'],
            comment= data['comment'],
        )

        reviews = restaurant.review_set.all()

        restaurant.numReviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating
        restaurant.rating = total / len(reviews)
        restaurant.save()

        return Response('Review Added')