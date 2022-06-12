from .models import Restaurant, Review
from .serializers import RestaurantSerializer, ReviewSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@api_view(['GET'])
def restaurant_list(request):
    search = request.query_params.get('find_desc')
    location = request.query_params.get('find_loc')
    if search == None:
        search = ''
    if location == None:
        location = ''
        print(location)
    restaurants = Restaurant.objects.filter(name__icontains=search, neighborhood__icontains=location)
    page = request.query_params.get('page')
    paginator = Paginator(restaurants, 5)

    try:
        restaurants = paginator.page(page)
    except PageNotAnInteger:
        restaurants = paginator.page(1)
    except EmptyPage:
        restaurants = paginator.page(paginator.num_pages)
    if page == None:
        page = 1
    page=int(page)
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response({'restaurants':serializer.data, 'page':page, 'pages':paginator.num_pages})


@api_view(['GET'])
def restaurant_detail(request, pk):
    try:
        restaurant = Restaurant.objects.get(id=pk)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RestaurantSerializer(restaurant)
    return Response(serializer.data)



@api_view(['DELETE', 'PUT'])
@permission_classes([IsAdminUser])
def restaurant_admin(request, pk):
    try:
        restaurant = Restaurant.objects.get(id=pk)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createRestaurantReview(request, pk):
    user = request.user
    restaurant = Restaurant.objects.get(id=pk)
    data = request.data
    print(user)
    alreadyExists = restaurant.review_set.filter(user=user).exists()
    if alreadyExists:
        content = {'detail': 'You have already reviewed this restaurant'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    elif data['rating'] == 0:
        content = {'detail': 'Please select rating'}
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

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editRestaurantReview(request, pk):
    user = request.user
    review = Review.objects.get(id=pk)
    data = request.data
    serializer = ReviewSerializer(review, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)